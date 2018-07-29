var app = new   Vue({
    el: "#choiceform",
    delimiters: ["{:",":}"],
    data: {
        choice: [],
        inputdata: "",
        maindata: "",
        show: false,
    },
    methods: {
        manipulate: function() {
            this.inputdata = this.inputdata.charAt(0).toUpperCase() + this.inputdata.slice(1)
            this.choice.push(this.inputdata.replace(",",""))
            this.inputdata = ""
            this.maindata = this.choice.toString()
        },
        removedata: function(value) {
            let index = this.choice.indexOf(value)
            this.choice.splice(index, 1)
            this.maindata = this.choice.toString()

        },
    },
})