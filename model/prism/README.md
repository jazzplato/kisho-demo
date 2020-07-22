# Probabilistic Modeling in Prism

## Why Prism?
> TL;DR: I need to do probablistic modeling to guess how the system is likely to evolve in the future.

One key reason why I choose to use Prism is that it can do the calculation of the probabilities based on the temporal logic I specify. 

## Two-Level of Modeling
In my design, there are two levels of system modeling: the system states and the system architectures.

### Observable Model: System States
The state of the system (idel, normal, critical, etc.) can be observed with the aid of the monitoring. Based on the statistics collected, we can update the probabilistic model (markov chain) in real-time. We can use PRISM to estimate the probability of going to certain states within a finite number of feedback-loop cycles

### Hidden Model: System Architetcure Implementations
Unlike the system states, the system architecture is far more difficult to determine. We then can use the system state model as the help to guess what is the optimal architecture based on the current state. We can connect both models in the form of a hidden-markov model.

## Markov Chain
Initially, the mapping between a system state and a system architecture implementation can be statically defined. Later on, due to the nature of the hidden-markov model, we can use ML to learn the mapping in the runtime.

## Role-Based Planning for Different Goals (MAGI)
A software system may have a number of conflicting goals, which are from the perspectives of different stakeholders of the system (users, business owners, developers, operator, etc.). In the planning phase of a homeostasis self-adaptive system, all these goals should be represented and considered, maybe in different weightages depending on the state of the system.



