# kisho-demo
An experiment and a demo for metabolic homeostasis self-adaptation systems.

## What is it?
It is for my independent study on the architectural-based self-adaptation system, under the supervision of [Prof. David Garlan](https://www.cs.cmu.edu/~garlan/) starting from the summer, 2020. Most of the research materials and inspirations are from the [CMU ABLE Group](http://www.cs.cmu.edu/~able/).

## What I want to achieve?
I want to try to explore the possibility to architect and establish a general purpose system with certain level of homeostasis self-adaptation capability. In specific, such self-adaptation include more than auto-scaling and service recovery (e.g. service rebooting and auto roll-back), but more on the architectural changes, like dynamically changing sync api dependencies to async, adding message queues to pass-through load balancers, etc. Of course, the keywords for such self-adaptation tactics are **dynamic** and **safe**.

## What I am proposing?
I am proposing a way to achieve homeostasis self-adaptation for software systems via metabolism.
> Metabolism consists of the sum of anabolism (construction) and catabolism (destruction) with the release of energy, and achieving a fairly constant internal environment (homeostasis).

In specific, I am proposing:
- the architecture of a system is not static, but of a number of variations; in Component-and-Connector views:
  - components are static
  - connectors can have a number heterogenous designs
- the architecture and the state of the system can be decribed using a Hidden Markov model, such that
  - the state of the system (e.g. idle, normal, critical, failed, etc.) can be observable with the monitored metrics
  - the state of the architecture can not be directly observed but can be inferred from the state of the system
  - the probabilities of the inter-state transformations can be updated dynamically alongside with the self-adaptation
- the decisions on where to go and when to go are vital
  - the analysis module in the MAPE-K model should come up with what is the next system and architecture state
  - more importantly, it should have the time in mind, i.e. how much in advance the system should prepare the architectural changes so that the changes can take effect **in time**
- *\*the tactics planning can involve a voting to balance out all the quality attributes on stake*
  - optional, but interesting hypothesis
  - maybe introduce personality-based voting
  - inspired by [MAGI](https://wiki.evageeks.org/Magi)

## What the name stands for?
It is named after a great Japanese architect, [Kisho Kurokawa](https://en.wikipedia.org/wiki/Kisho_Kurokawa), a pioneer in the metabolism movement in the achitecture domain in Japan in 1960s. Here quotes the famous Metabolism Manifesto, which I find resonant with the research direction I am heading:
> Metabolism is the name of the group, in which each member proposes further designs of our coming world through his concrete designs and illustrations. We regard human society as a vital process - a continuous development from atom to nebula. The reason why we use such a biological word, metabolism, is that we believe design and technology should be a denotation of human society. We are not going to accept metabolism as a natural process, but try to encourage active metabolic development of our society through our proposals.

## What is different from the mainstream self-adaptation?
### Model-based VS. Rule-based
Unlike most of the self-adaptation, such as [kubernetes](https://kubernetes.io/) for containers and [AWS](https://aws.amazon.com/) for cloud instances, of which the self-adapation is rule-based, this research focus on the model-based self-adaptation. It has the following highlights:
- use state machines (or Markov Decision Process) to represent system states
- use formal methods for analysis
- have a architecture model as the common knowledge
- follow [MAPE-K](https://ieeexplore.ieee.org/document/7194653) model as the high-level direction
### Reactive VS. Proactive
Due to the rule-based nature, most of the current self-adaptation is reactive, where the response time (latency) can be critical to the success of the adaptation. There is another way out actually: to do the self-adaptation proactively, aka. to achieve homeostasis of the systems. This requires analysis and planning in advance.

## What are the quality attributes on the stake?
Simply speaking, **anything**. Currently, the mainstream self-adapation only can address a handful of quality attributes, like costs(e.g. scale in), availability (e.g. roll-back), performance like throughput (e.g. scale out). However, many other quality attributes, like reliability, safety, security, etc. I believe it is possible to incorporate those quality attributes in the on-the-fly in the self-adaptation processes.
