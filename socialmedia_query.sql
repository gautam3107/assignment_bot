SELECT p.post_id, p.user_id, p.content, p.created_at
FROM posts p
JOIN friends f ON p.user_id = f.friend_id
WHERE f.user_id = :current_user_id
ORDER BY p.created_at DESC;