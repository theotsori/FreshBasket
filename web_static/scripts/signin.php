<?php
// Database connection parameters
$servername = 'localhost';
$username = 'fresh_dev_db';
$password = 'fresh_dev_pwd';
$dbname = 'fresh_basket';

// Retrieve the user credentials from the request
$email = $_POST['email'];
$password = $_POST['password'];

// Create a new MySQL connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
  die('Connection failed: ' . $conn->connect_error);
}

// Prepare the SQL statement to check if the user exists and the password is correct
$stmt = $conn->prepare('SELECT * FROM users WHERE email = ?');
$stmt->bind_param('s', $email);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows === 1) {
  $row = $result->fetch_assoc();
  if (password_verify($password, $row['password'])) {
    // Authentication successful
    $response = array('success' => true, 'message' => 'Authentication successful');
  } else {
    // Invalid password
    $response = array('success' => false, 'message' => 'Invalid password');
  }
} else {
  // User not found
  $response = array('success' => false, 'message' => 'User not found');
}

// Send the response as JSON
header('Content-Type: application/json');
echo json_encode($response);

// Close the database connection
$stmt->close();
$conn->close();
?>
