var data1 = new Date("2023-07-01");
   var data2 = new Date("2023-07-15");
   
   if (data1.getTime() < data2.getTime()) {
     console.log("data1 é anterior a data2");
   } else if (data1.getTime() > data2.getTime()) {
     console.log("data1 é posterior a data2");
   } else {
     console.log("data1 é igual a data2");
   }