import redis


class RedisOperation:
    redis_obj = redis.StrictRedis(host='localhost', port=6379, db=0)

    def check_link(self, link, user_id):
        try:
            redis_link = RedisOperation.redis_obj.get(user_id)
            if redis_link.decode("utf-8") == link:
                return True
            return False
        except:
            return False

    def set_link(self, link, user_id):
        try:
            RedisOperation.redis_obj.set(user_id, link)
            RedisOperation.redis_obj.expire(user_id, 86400)
            return True
        except:
            return False
