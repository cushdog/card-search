import { useEffect } from "react";

const KeyLogger = () => {
  useEffect(() => {
    let swipeData = "";

    const handleKeyPress = (event) => {
      const { key } = event;

      if (key === "\n") {
        console.log("Swipe data:", swipeData);
        swipeData = "";
      } else {
        swipeData += key;
      }

    };

    document.addEventListener("keydown", handleKeyPress);

    return () => {
      document.removeEventListener("keydown", handleKeyPress);
    };
  }, []);

  return null;
};

export default KeyLogger;
