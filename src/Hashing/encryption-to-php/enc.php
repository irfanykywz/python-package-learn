<?php
// https://gist.github.com/ahbanavi/ff3c0711b45f5056f821c00438af8f67
// https://stackoverflow.com/questions/38716613/generate-a-single-use-token-in-php-random-bytes-or-openssl-random-pseudo-bytes

//  gen key
var_dump(bin2hex(openssl_random_pseudo_bytes(32)));

const PASSPHRASE = '06bebe45f8547902f83222361f1281e620b22716ecb9c41aaaac7526d8228e53';
// use 'openssl rand-hex 32' to generate key, same with python

function encrypt(array $data): string
{
    $data_json_64 = base64_encode(json_encode($data));
    $secret_key = hex2bin(PASSPHRASE);
    $iv = openssl_random_pseudo_bytes(openssl_cipher_iv_length('aes-256-gcm'));
    $tag = '';
    $encrypted_64 = openssl_encrypt($data_json_64, 'aes-256-gcm', $secret_key, 0, $iv, $tag);
    $json = new stdClass();
    $json->iv = base64_encode($iv);
    $json->data = $encrypted_64;
    $json->tag = base64_encode($tag);
    return base64_encode(json_encode($json));
}

function decrypt(string $data): array
{
    $secret_key = hex2bin(PASSPHRASE);
    $json = json_decode(base64_decode($data), true);
    $iv = base64_decode($json['iv']);
    $tag = base64_decode($json['tag']);
    $encrypted_data = base64_decode($json['data']);
    $decrypted_data = openssl_decrypt($encrypted_data, 'aes-256-gcm', $secret_key, OPENSSL_RAW_DATA, $iv, $tag);
    return json_decode(base64_decode($decrypted_data),True);
}

$dec = decrypt('eyJpdiI6ICJQV3NrOHdNMjdWK1N6eHI4NW5POG93PT0iLCAiZGF0YSI6ICI0eHdTTWpUUUkxZTdTbE9iNkVBNG53PT0iLCAidGFnIjogInNyU3JjRXpLKzZTTUo1Q1ZqWHcwV2c9PSJ9');
var_dump($dec);

/*
array(1) {
  [0]=>
  string(5) "babhi"
}
*/