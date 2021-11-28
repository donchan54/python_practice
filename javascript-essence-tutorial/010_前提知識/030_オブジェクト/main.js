let obj = {
    prop1: "Value1",
    prop2: "Value2",
    prop3: function() {
        console.log('Value3');
    },
    prop4: {
        prop5: "Value5"
    }
}
obj.prop3();

obj.prop6 = "Value6";
console.log(obj);