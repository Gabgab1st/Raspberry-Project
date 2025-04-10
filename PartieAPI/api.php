<?php
// Connexion à la base de données "cube2"
$pdo = new PDO('mysql:host=localhost;dbname=cube2', 'root', 'root');

// Vérifie si la méthode de la requête est POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    // Récupérer les données envoyées en JSON (si c'est un envoi JSON)
    $data = json_decode(file_get_contents("php://input"), true);

    // Vérifie que les données nécessaires sont présentes
    if (isset($data['temperature']) && isset($data['humidite'])) {
        
        // Récupérer les valeurs de température et d'humidité
        $temperature = $data['temperature'];
        $humidite = $data['humidite'];
        
        // Préparer et exécuter la requête SQL d'insertion
        $stmt = $pdo->prepare("INSERT INTO mesures (temperature, humidite) VALUES (?, ?)");
        $stmt->execute([$temperature, $humidite]);
        
        // Retourner une réponse JSON
        echo json_encode(["status" => "success", "message" => "Données insérées avec succès."]);
    } else {
        // Si les données ne sont pas complètes
        echo json_encode(["status" => "error", "message" => "Données manquantes."]);
    }

} else {
    // Si la requête n'est pas une méthode POST
    echo json_encode(["status" => "error", "message" => "Méthode HTTP non autorisée."]);
}
?>
