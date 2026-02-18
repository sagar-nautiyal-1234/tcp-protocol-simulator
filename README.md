<h1 align="center">📡 TCP Protocol Simulator</h1>

<p align="center">
<b>Python • Tkinter • Event-Driven Architecture • Protocol Simulation</b><br>
An interactive desktop application that visualizes how TCP actually works internally.
</p>

<hr>

<h2>🧠 Overview</h2>

<p>
The <b>TCP Protocol Simulator</b> is a desktop GUI application that models and visualizes the internal behavior of the Transmission Control Protocol (TCP). Instead of transmitting real network packets, the system simulates transport-layer communication so users can observe how TCP establishes connections, sends data, handles failures, and maintains reliability.
</p>

<p>
The simulator transforms abstract networking concepts into live visual processes, allowing users to see packet flow, acknowledgements, retransmissions, and state transitions in real time.
</p>

<hr>

<h2>⚙️ Core Features</h2>

<h3>Connection Lifecycle Simulation</h3>
<ul>
<li>Three-way handshake (SYN → SYN-ACK → ACK)</li>
<li>Connection termination (FIN → ACK)</li>
<li>Real-time state transitions</li>
</ul>

<h3>Reliability Mechanisms</h3>
<ul>
<li>Sequence number tracking</li>
<li>Acknowledgement handling</li>
<li>Timeout detection</li>
<li>Automatic retransmission</li>
</ul>

<h3>Flow Control</h3>
<ul>
<li>Sliding window protocol implementation</li>
<li>In-flight packet monitoring</li>
<li>Window-full blocking logic</li>
</ul>

<h3>Transport Layer Simulation</h3>
<ul>
<li>Artificial latency injection</li>
<li>Asynchronous delivery</li>
<li>Delayed packet arrival</li>
<li>Simulated network conditions</li>
</ul>

<h3>Visualization Engine</h3>
<ul>
<li>Animated packet movement between client and server</li>
<li>Directional indicators</li>
<li>Retransmission animations</li>
<li>Timeout alerts</li>
<li>Live connection state display</li>
</ul>

<hr>

<h2>🛠 Technology Stack</h2>

<ul>
<li><b>Language:</b> Python</li>
<li><b>GUI Framework:</b> Tkinter</li>
<li><b>Architecture:</b> Modular layered architecture</li>
<li><b>Concurrency:</b> threading</li>
<li><b>Data Modeling:</b> dataclasses</li>
</ul>

<h3>Design Principles Used</h3>
<ul>
<li>Event-driven architecture</li>
<li>Event bus communication pattern</li>
<li>Separation of concerns</li>
<li>Modular system design</li>
<li>Layer isolation</li>
</ul>

<hr>

<h2>🏗 System Architecture</h2>

<p>The simulator is structured similarly to a real protocol engine:</p>

<pre>
GUI Layer
   ↓
Event Bus
   ↓
Protocol Engine
   ↓
Transport Simulation
   ↓
Packet Model
</pre>

<p>
Each layer communicates exclusively through events, ensuring independence, extensibility, and maintainability.
</p>

<hr>

<h2>🧩 Computer Science Concepts Demonstrated</h2>

<ul>
<li>Finite State Machines</li>
<li>Protocol Design & Modeling</li>
<li>Concurrent Programming</li>
<li>Asynchronous Systems</li>
<li>Simulation Engineering</li>
<li>Systems-Level Thinking</li>
<li>Layered Software Architecture</li>
<li>Event-Driven Systems</li>
</ul>

<hr>

<h2>🚀 Why This Project Stands Out</h2>

<p>Most networking projects simply send data using sockets.</p>

<p><b>This project instead simulates how TCP works internally.</b></p>

<ul>
<li>Models protocol behavior rather than using network APIs</li>
<li>Implements real TCP logic such as retransmission and flow control</li>
<li>Visualizes normally invisible network operations</li>
<li>Demonstrates deep understanding of transport-layer mechanics</li>
</ul>

<hr>

<h2>▶️ Running the Application</h2>

<pre>
python main.py
</pre>

<p><b>Requirements:</b></p>
<ul>
<li>Python 3.x</li>
<li>Tkinter (preinstalled with most Python distributions)</li>
</ul>

<hr>

<h2>📌 Purpose of the Project</h2>

<p>
This simulator was built to bridge the gap between theoretical networking concepts and real protocol behavior by providing a visual and interactive representation of TCP mechanics. It serves both as an educational visualization tool and as a demonstration of practical systems programming skills.
</p>

<hr>

<h2>📄 Resume Description</h2>

<blockquote>
Built an interactive TCP protocol simulator with animated packet visualization, implementing handshake, retransmission, sliding window flow control, and timeout mechanisms using Python and event-driven architecture.
</blockquote>

<hr>

<h2 align="center">🎯 Summary</h2>

<p align="center">
The TCP Protocol Simulator functions as a miniature protocol engine that models real TCP logic while remaining fully observable, interactive, and modular.
</p>

<p align="center"><b>⭐ Star this repository if you found it interesting!</b></p>
