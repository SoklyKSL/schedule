Telegram.WebApp.ready();

const user = Telegram.WebApp.initDataUnsafe.user;
const statusEl = document.getElementById("status");

if (!user) {
  statusEl.innerText = "User info not available.";
} else {
  const data = {
    telegram_id: user.id,
    name: `${user.first_name} ${user.last_name || ''}`,
    phone_number: null  // will be set via /start bot flow
  };

  fetch(window.location.origin + "/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(result => {
    statusEl.innerText = result.status === "new"
      ? "You have been registered!"
      : "Welcome back!";
  })
  .catch(() => {
    statusEl.innerText = "Error connecting to backend.";
  });
}
