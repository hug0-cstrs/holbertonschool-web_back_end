export default function updateStudentGradeByCity(grades, city, newGrades) {
  if (!Array.isArray(grades)) {
    return [];
  }
  return grades.map((student) => {
    const newGrade = newGrades.filter((item) => item.studentId === student.id);
    if (newGrade.length > 0) {
      return { ...student, grade: newGrade[0].grade };
    }
    return { ...student, grade: 'N/A' };
  });
}
