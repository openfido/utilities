const fs = require('fs');

// The first two args are what call this file and are not needed
// The third arg onward is used to find the directories used in the function
let args = process.argv.slice(2);

args.forEach(function (val, index, array) {

    // reads the directory for contained files
    fs.readdir(val, function (err, files) {
        //handling error
        if (err) {
            return console.log('Unable to scan directory: ' + err);
        } 
        //listing all files using forEach
        files.forEach(function (file) {
            // Lists the file being searched for download urls
            console.log(file);

            fs.readFile(`${val}/${file}`, (err, data) => {
                if (err)  {
                    console.error('There is an issue reading the file:', err);
                    throw err;
                }

                // File data is converted into an array buffer when read
                // It needs to be returned to a string format to be parsed
                const str = String.fromCharCode.apply(null, new Uint16Array(data));

                // Use a regex to find all URLs, logged for users to read
                var urlRegex = /(https?:\/\/[^\s]+)/g;
                const array = typeof str === 'string' ? str.match(urlRegex) : [];
                console.log(array);
                if (typeof str !== 'string') {
                    console.error('Error in parse, expected a string but received:', typeof str);
                    console.error('with a value of:', str)
                }

                //Potential Error Checks
                if (array === null) {
                    console.error('No URL matches were found in the provided files.')
                }

                // Generate a wget friendly file full of properly spaced URLs to download!
                if (array !== null && Array.isArray(array)) {
                    let fileContent = array.join('\n');
                    fileContent += '\n';
                    fs.appendFileSync('./curls.txt', fileContent);                   
                } else {
                    let fileContent = '';
                    fs.appendFileSync('./curls.txt', fileContent);
                }
              }); 
        });
    });
  });
