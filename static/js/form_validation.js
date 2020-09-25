const fname = document.getElementById('first_name')
const lname = document.getElementById('last_name')
const about = document.getElementById('about')
const qualification = document.getElementById('qualification')
const img = document.getElementById('profile_image')
const form = document.getElementById('form')
const errorText = document.getElementById('error')

form.addEventListener('submit', (e) => {
  let errorMessage = []
  if (fname.value.trim() == "") {
    errorMessage.push('Please enter valid first name.')
  }
  
  if (lname.value.trim() == "") {
    errorMessage.push('Please enter valid last name.')
  }
  
  if (about.value.trim() == "") {
    errorMessage.push('Please enter some information about yourself.')
  }
  
  if (qualification.value.trim() == "") {
    errorMessage.push('Please enter a qualification.')
  }
  
  if (img.value.trim() == "") {
    errorMessage.push('Please enter a valid image link.')
  }

  if (errorMessage.length > 0) {
    e.preventDefault()
    errorText.innerText = errorMessage.join(' ')
  }
})