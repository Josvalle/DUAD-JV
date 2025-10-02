const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}

let gradesList = [];
const  firstName = student.name;

for (const i of student.grades){
    gradesList.push(i.grade)
};

let sumOfGrade = 0
for (const i of gradesList){
    sumOfGrade += i
}
const average = sumOfGrade/gradesList.length

sortList = gradesList.sort((a,b)=> a>b ? -1 :1);
const highGrade = sortList[0];
reverseList = gradesList.reverse()
const lowGrade = reverseList[0]

const foundHighest = student.grades.find(element => element.grade === highGrade )
const foundLowest = student.grades.find(element => element.grade === lowGrade)

const result ={
    name: firstName,
    gradeAvg: average,
    highesGrade: foundHighest.name,
    lowestGrade: foundLowest.name
}

console.log(result)