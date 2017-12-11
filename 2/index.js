const fs = require('fs');
const readline = require('readline');

function part_one(filename) {
    return new Promise((resolve, reject) => {
        let result = 0;

        const lineReader = readline.createInterface({
            input: fs.createReadStream(filename)
        });
        
        lineReader.on('line', function (line) {
            let numbers = line.split('\t');
            const max = Math.max.apply(null, numbers);
            const min = Math.min.apply(null, numbers);
            
            result += (max - min);
        });
        
        lineReader.on('close', () => {
            resolve(result);
        });
    });
}

function part_two(filename) {
    return new Promise((resolve, reject) => {
        let result = 0;

        const lineReader = readline.createInterface({
            input: fs.createReadStream(filename)
        });
        
        lineReader.on('line', function (line) {
            const numbers = line.split('\t');

            for (let i = 0; i < numbers.length; i++) {
                for (let j = 0; j < numbers.length; j++) {
                    if (i !== j && numbers[i] % numbers[j] === 0) {
                        result += numbers[i] / numbers[j];
                    }
                }
            }
        });
        
        lineReader.on('close', () => {
            resolve(result);
        });
    });
}

part_one('./input_file.txt').then((result) => {
    console.log(result);
});

part_two('./input_file.txt').then((result) => {
    console.log(result);
});