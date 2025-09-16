const VideoStream: React.FC = () => {
  return (
    <div>
      <img
        src="http://localhost:5000/camera"
        alt="Live stream"
        style={{ width: "640px", height: "480px", border: "2px solid black" }}
      />
    </div>
  );
};

export default VideoStream;