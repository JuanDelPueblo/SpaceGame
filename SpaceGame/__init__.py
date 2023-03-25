from gym.envs.registration import register

register(
    id='SpaceGame/SpaceshipGame-v0',
    entry_point='SpaceGame.envs:SpaceshipGameEnv',
    max_episode_steps=300,
)