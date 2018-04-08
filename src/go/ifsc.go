// package ifsc
package main

import "encoding/json"
import "fmt"
import "strings"
import "strconv"
import "io/ioutil"

// DATA has entire IFSC data in a map
// This helps in faster lookup by avoid file close/open each time
var DATA = ReadData("../IFSC.json")

func arrayElemsToString(arr []interface{}) []string {
	bucket := make([]string, len(arr))

	for _, each := range arr {
		valString, okString := each.(string)
		valueFloat64, okFloat64 := each.(float64)

		if okFloat64 {
			bucket = append(bucket, strconv.Itoa(int(valueFloat64)))
		} else if okString { // this is a string
			bucket = append(bucket, valString)
		} else {
			panic(fmt.Sprint("Some unknown type in branch code", each))
		}
	}

	return bucket
}

// ReadData reads IFSC.json and returns corresponding Go structure
func ReadData(datafile string) map[string][]string {
	content, err := ioutil.ReadFile(datafile)
	if err != nil {
		fmt.Println("Error: Cannot read datafile", datafile)
		panic(err)
	}

	data := make(map[string][]interface{})
	if json.Unmarshal(content, &data) != nil {
		fmt.Println("Error unmarshalling json", datafile)
		panic(err)
	}

	result := make(map[string][]string)
	for k := range data {
		result[k] = arrayElemsToString(data[k])
	}

	return result
}

// Validate takes a ifsc code and returns true if the code is valid
// and false otherwise
func Validate(code string) bool {
	if len(code) != 11 {
		return false
	}

	if code[4:5] != "0" {
		return false
	}

	bankCode := strings.ToUpper(code[0:4])

	branchCodeStr := strings.ToUpper(code[5:])
	newArr := []interface{}{branchCodeStr}
	branchCode := arrayElemsToString(newArr)[1]
	bc := arrayElemsToString(newArr)

	if _, exists := DATA[bankCode]; !exists {
		return false
	}

	for _, givenCode := range DATA[bankCode] {
		if givenCode == branchCode {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println("This is a golang program")
	fmt.Println(Validate("SBIN0006992"))
	fmt.Println(Validate("SBIN0098992"))
	fmt.Println(Validate("SBEN0006992"))
}
