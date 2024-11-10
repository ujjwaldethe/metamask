// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;
contract StudentData{
    struct Student{
        uint id;
        string name;
        uint age;
        string major;
    }
    Student[] private student;
    fallback() external payable { }
    function addStudent(uint _id,string memory _name,uint _age,string memory _major) public{
        Student memory newStudent = Student(_id, _name ,_age,_major);
        student.push(newStudent);
    }
    function getStudent(uint _id) view public returns(Student memory)
    {
        for(uint i=0;i<student.length;i++)
        {
            if(student[i].id== _id)
            {
                return student[i];
            }
        }
        return Student(0," ",0," ");
    }
    function getAllStudents()public view returns(Student[] memory){
            return student;
    }
    function deleteStudent(uint _id) public returns (bool)
    {
        for(uint i=0;i<student.length;i++)
        {
            if(student[i].id==_id)
            {
                    student[i]=student[student.length-1];
                    student.pop();
                    return true;
            }
            
        }
        return false;
    }
}