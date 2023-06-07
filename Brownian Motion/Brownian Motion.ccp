
#include <SFML/Graphics.hpp>
#include <random>

int main()
{
    const int WINDOW_WIDTH = 800;
    const int WINDOW_HEIGHT = 600;
    const int NUM_PARTICLES = 100;
    const float PARTICLE_RADIUS = 2.0f;
    const float MAX_VELOCITY = 0.5f;

    sf::RenderWindow window(sf::VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), "Brownian Motion Animation");
    sf::Clock clock;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> dis(-MAX_VELOCITY, MAX_VELOCITY);
    std::vector<sf::CircleShape> particles(NUM_PARTICLES);

    // Initializing particles at random positions
    
    for (auto& particle : particles)
    {
        particle.setRadius(PARTICLE_RADIUS);
        particle.setPosition(dis(gen) + WINDOW_WIDTH / 2, dis(gen) + WINDOW_HEIGHT / 2);
        particle.setFillColor(sf::Color::Blue);
    }

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        float deltaTime = clock.restart().asSeconds();

        // Update particle positions
        for (auto& particle : particles)
        {
            float dx = dis(gen) * deltaTime;
            float dy = dis(gen) * deltaTime;
            particle.move(dx, dy);
        }

        window.clear(sf::Color::White);

        // Draw the particles
        
        for (const auto& particle : particles)
        {
            window.draw(particle);
        }

        window.display();
    }

    return 0;
}
