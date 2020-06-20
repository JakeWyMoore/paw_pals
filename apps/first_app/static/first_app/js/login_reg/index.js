const login = document.getElementById('login');
const register = document.getElementById('register');
const card = document.getElementById('card');

register.addEventListener('click', () => {
  login.classList.remove('selected');
  register.classList.add('selected');
  card.classList.add("extend");
})

login.addEventListener('click', () => {
  login.classList.add('selected');
  register.classList.remove('selected');
  card.classList.remove("extend");
})