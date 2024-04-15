function zeros(n) {
    let count = 0;
    while (n >= 5) {
        n = Math.floor(n / 5);
        count += n;
        console.log(n)
    }
    return count;
}

// const zeros = n => n / 5 < 1 ? 0 : Math.floor(n / 5) + zeros(n / 5)


// function zeros (n) {
//   n = ~~(n/5);
//   return  n + (n<5 ? 0 : zeros(n));
// } 

console.log(zeros(25))
 