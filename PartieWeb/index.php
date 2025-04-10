<?php
$pdo = new PDO('mysql:host=localhost;dbname=cube2', 'root', 'root');
$req = $pdo->query("SELECT * FROM mesures ORDER BY date DESC LIMIT 10");

?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Données des Capteurs</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <h1>Mesure de la Température et de l'Humidité</h1>

    <!-- Tableau des données -->
    <table>
        <tr>
            <th>Date</th>
            <th>Température (°C)</th>
            <th>Humidité (%)</th>
        </tr>

        <?php while ($row = $req->fetch()) : ?>
        <tr>
            <td><?= $row['date'] ?></td>
            <td><?= $row['temperature'] ?>°C</td>
            <td><?= $row['humidite'] ?>%</td>
        </tr>
        <?php endwhile; ?>
    </table>

</body>
</html>
