// const fs = require('fs')
// fs.readFile('/home/navgurukul/Desktop/basic/streammod/input.txt', (err, data) => {
// 	if (err) {
// 		console.error(err)
// 		return
// 	}
// 	console.log(data.toString())
// })

////////////////////////////////////////////////////

// const fs = require('fs')

// fs.writeFile('README.md', 'Hello World', (err) => {
// 	if (err) {
// 		console.error(err)
// 		return
// 	}
// 	console.log('wrote to file successfully')
// })
/////////////////////////////////////////////

// const fs = require('fs')
// fs.writeFile('subhash.txt', 'Hello World', (err) => {
// 	if (err) {
// 		console.error(err)
// 		return
// 	}
// 	console.log('wrote to file successfully')
// })

////////////////////////////////////////

// const fs = require('fs')

// // The writeFileSync API takes the location of the file
// // and the contents to be written to it
// fs.writeFileSync('README.md', 'Hello Sync API!')

// // The readFileSync API reads the file and returns a
// // Buffer, whose `toString` method gives the string
// // representation of the file
// console.log(fs.readFileSync('README.md').toString())

//////////////////////////////////////////////

// const fs = require('fs')
// fs.writeFileSync('/home/navgurukul/Desktop/basic/streammod/input.txt', 'Hello Sync API!')

// console.log(fs.readFileSync('/home/navgurukul/Desktop/basic/streammod/input.txt').toString())

////////////////////////////////////////////////////////////



// const fs = require('fs')
// const startTime = new Date()

// // create a read stream from the `words.txt` file
// const rStream = fs.createReadStream('input.txt')

// // initialize total word count
// let total = 0

// // the `on data` method registers a handler for everytime we
// // receive new data from the file stream
// rStream.on('data', b => {
// 	// `b` here is the chunk of data received from the
// 	// file stream
// 	const bStr = b.toString()
// 	// We split the string by spaces and new lines and add it to the
// 	// total -- we subtract one because of the extra space/newline/broken word
// 	// at the end of the chunk
// 	// we shouldn't do this for the last chunk of data, which we handle later
// 	total += bStr.split(/[\s\n]+/).length - 1
// })

// rStream.on('end', () => {
// 	// Finally, the `on end` handler is called once the data stream completes

// 	// we add one to the total, because we shouldn't subtract 1 from the last
// 	// chunk of data in the `data` handler, for which we're compensating here
// 	console.log('total words:', total + 1)


// 	// Print the total time taken, as well as the total used program memory
// 	console.log('total time:', (new Date()) - startTime)

// 	const memoryUsedMb = process.memoryUsage().heapUsed / 1024 / 1024
// 	console.log('the program used', memoryUsedMb, 'MB')
// })

////////////////////////////////////////////////////


// const fs = require('fs')

// fs.readdir('./', (err, files) => {
// 	if (err) {
// 		console.error(err)
// 		return
// 	}

// 	console.log('files: ', files)
// })
/////////////////////////////

// const fs = require('fs')
// fs.readdir('./', { withFileTypes: true }, (err, files) => {
// 	if (err) {
// 		console.error(err)
// 		return
// 	}

// 	console.log('files: ')
// 	files.forEach(file => {
// 		// the `isDirectory` method returns true if the entry is a directory
// 		const type = file.isDirectory() ? '📂' : '📄'
// 		console.log(type, file.name)
// 	})
// })

/////////////////////////////////////

// const fs = require('fs')

// fs.mkdir('./newdir', err => {
// 	if (err) {
// 		console.error(err)
// 		return
// 	}

// 	console.log('directory created')
// })

/////////////////////////////////////

// const fs = require('fs')

// fs.rmdir('./newdir', err => {
// 	if (err) {
// 		console.error(err)
// 		return
// 	}

// 	console.log('directory deleted')
// })
/////////////////////////////////////////

