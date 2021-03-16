## 1. Printing User Input ##

/home/dq$ echo "This is a command line interface."

## 2. Redirecting Output with > ##

/home/dq$ grep -hi ',Math' /home/dq/rg_data/* >/home/dq/math_data

## 3. Redirecting Output with >> ##

/home/dq$ grep -hi ',Math' /home/dq/rg_data/* >>math_dataset

## 4. Creating Empty Files ##

/home/dq$ touch on e

## 5. Why Pipelines? ##

/home/dq$ cut -d"," -f1,2,5 math_dataset

## 6. Using Pipelines ##

/home/dq$ zen | grep "better"

## 7. The Unix Philosophy ##

/home/dq/rg_data$ sort -u * | wc -l

## 8. Trying to Redirect Errors ##

/home/dq/rg_data$ echo something >/dev/null