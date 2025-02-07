html {
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
}

body {
    background-color: #0e1011;
    color: #eaeaea;
    margin: 0;
    padding: 0;
}

#navbar {
    position: fixed;
    left: 0;
    top: 0;
    width: 250px;
    height: 100vh;
    background-color: rgba(14, 16, 17, 0.9);
    padding: 20px;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.3);
    z-index: 1000;
}

#navbar header {
    font-size: 1.5rem;
    color: #fff;
    margin-bottom: 30px;
    font-weight: 600;
    text-align: center;
}

#navbar ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

#navbar ul li {
    margin: 10px 0;
    cursor: pointer;
    transition: all 0.3s ease;
}

#navbar ul li:hover {
    background-color: rgba(255, 255, 255, 0.05);
    padding-left: 5px;
}

#navbar ul li a {
    color: #eaeaea;
    text-decoration: none;
    font-size: 0.9rem;
}

#navbar ul li a:hover {
    color: #fff;
}

#main-doc {
    margin-left: 250px;
    padding: 40px;
    background-color: #1e2123;
}

#main-doc section {
    margin-bottom: 40px;
    padding: 30px;
    background-color: #23272a;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

#main-doc header {
    font-size: 1.3rem;
    color: #fff;
    margin-bottom: 20px;
    border-bottom: 2px solid #2c3e50;
}

#main-doc p {
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 1rem;
}

code {
    color: #CCCCCC;
    background-color: #1d1d1d;
    padding: 4px 8px;
    border-radius: 4px;
    font-family: 'Consolas', monospace;
    display: inline-block;
}

@media only screen and (max-width: 815px) {
    #navbar {
        width: 100%;
        margin: 0;
        padding: 0;
        position: fixed;
        top: 0;
        left: 0;
        background-color: rgba(14, 16, 17, 0.95);
        backdrop-filter: blur(10px);
    }

    #navbar ul {
        height: calc(100vh - 80px);
        padding: 30px 20px;
        box-sizing: border-box;
        overflow-y: auto;
        display: block;
    }

    #navbar ul li {
        display: block;
        width: 100%;
        padding: 10px 30px;
    }

    #main-doc {
        margin-left: 0;
        margin-top: 50px;
        padding: 20px 10px;
    }

    #main-doc section {
        margin-bottom: 30px;
    }
}