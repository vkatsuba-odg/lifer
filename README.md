# lifer
Schema generator prototype from LIF data

# Requirements
  * Python version **3.6.x** or higher
  * Install **fastavro**
  * Install **rec_avro**

# Run `schemer.py`
```sh
$ git clone https://github.com/vkatsuba-odg/lifer.git
$ cd lifer
$ ./schemer.py -l test.lif
$ cat schemer_output.json
```

# Run `lifer.py`
```sh
$ git clone https://github.com/vkatsuba-odg/lifer.git
$ cd lifer
$ ./lifer.py -l test.lif
$ cat schema.json
{
   "type":"record",
   "name":"test",
   "fields":[
      {
         "type":"array",
         "name":"month_over_month",
         "items":{
            "type":"record",
            "name":"month_over_month_item",
            "fields":[
               {
                  "type":"string",
                  "name":"Label"
               },
               {
                  "type":"float",
                  "name":"CPI Inflation"
               },
               {
                  "type":"float",
                  "name":"Core CPI Inflation"
               },
               {
                  "type":"float",
                  "name":"PCE Inflation"
               },
               {
                  "type":"float",
                  "name":"Core PCE Inflation"
               },
               {
                  "type":"string",
                  "name":"Actual CPI Inflation"
               },
               {
                  "type":"string",
                  "name":"Actual Core CPI Inflation"
               },
               {
                  "type":"string",
                  "name":"Actual PCE Inflation"
               },
               {
                  "type":"string",
                  "name":"Actual Core PCE Inflation"
               }
            ]
         }
      },
      {
         "type":"array",
         "name":"year_over_year",
         "items":{
            "type":"record",
            "name":"year_over_year_item",
            "fields":[
               {
                  "type":"string",
                  "name":"Label"
               },
               {
                  "type":"float",
                  "name":"CPI Inflation"
               },
               {
                  "type":"float",
                  "name":"Core CPI Inflation"
               },
               {
                  "type":"float",
                  "name":"PCE Inflation"
               },
               {
                  "type":"float",
                  "name":"Core PCE Inflation"
               },
               {
                  "type":"string",
                  "name":"Actual CPI Inflation"
               },
               {
                  "type":"string",
                  "name":"Actual Core CPI Inflation"
               },
               {
                  "type":"string",
                  "name":"Actual PCE Inflation"
               },
               {
                  "type":"string",
                  "name":"Actual Core PCE Inflation"
               }
            ]
         }
      }
   ]
}
```
