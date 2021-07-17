const axios = require("axios");
const fs = require("fs");
const rL = require("readline-sync");

api = axios.get("http://saral.navgurukul.org/api/courses")
api.then(response => {
    var apiData = response.data
    index = 1
    for(let i of apiData['availableCourses']){
        console.log(index+ " " + i['name'])
        index++
    }
    var course = rL.question("Enter course number : ")
    // console.log(apiData)
    // console.log(apiData['availableCourses'][course-1]['name'])
    var id = apiData['availableCourses'][course-1]['id']
    return (id)
})
.then((id) => {
    var url = "http://saral.navgurukul.org/api/courses/"+id+"/exercises"
    courseApi = axios.get(url);
    courseApi.then(response => {
        courseData = response.data['data'];
        var childExercisesList = []
        index = 1
        var slugDict = {}
        for(let k of courseData){
            slugDict[index] = k['slug']
            console.log(index + " "+k['name'])
            if(k['childExercises'].length>0){

                index2 = 1
                for(let m of k['childExercises']){
                    slugDict[index+"."+index2] = m['slug']
                    console.log(index+"."+index2+" "+m['name']);
                    index2++
                }
            }
            index++
        }
        return (slugDict)
    })
    .then((slugDict) => {
        var userSlug = rL.question("Enter exercise : ")
        getSlug = slugDict[userSlug]
        var url2 = "http://saral.navgurukul.org/api/courses/5/exercise/getBySlug?slug="+getSlug
        slugApi = axios.get(url2);
        slugApi.then(response =>{
            console.log(response.data['content'])
        })

    })
    courseApi.catch(err => {
        console.log(err.response.data);
    })
});
api.catch(err => {
    console.log(err.response.data)
});