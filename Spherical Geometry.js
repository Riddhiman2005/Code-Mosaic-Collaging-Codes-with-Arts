

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.PerspectiveCamera;
import javafx.scene.Scene;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.shape.CullFace;
import javafx.scene.shape.Mesh;
import javafx.scene.shape.MeshView;
import javafx.scene.shape.Sphere;
import javafx.scene.transform.Rotate;
import javafx.stage.Stage;

public class Main extends Application {
    private static final double CAM_SPEED = 1.0;
    private static final double FOV = 45.0;
    private static final double CAM_DISTANCE = 8.0;
    private static final double MOUSE_SPEED = 0.1;
    private static final double ROTATION_SPEED = 2.0;

    private PerspectiveCamera camera;
    private Sphere sphere;
    private double camYaw = 0.0;
    private double camPitch = 0.0;
    private double mouseX = 0.0;
    private double mouseY = 0.0;

    @Override
    public void start(Stage primaryStage) {
        Group root = new Group();
        Scene scene = new Scene(root, 800, 600, true);
        scene.setFill(Color.BLACK);
        scene.setOnMousePressed(this::handleMousePressed);
        scene.setOnMouseDragged(this::handleMouseDragged);
        scene.setOnKeyPressed(this::handleKeyPressed);

        camera = new PerspectiveCamera(true);
        camera.setNearClip(0.1);
        camera.setFarClip(1000.0);
        camera.setFieldOfView(FOV);
        camera.getTransforms().add(new Rotate(-camYaw, Rotate.Y_AXIS));
        camera.getTransforms().add(new Rotate(-camPitch, Rotate.X_AXIS));
        camera.setTranslateZ(-CAM_DISTANCE);

        sphere = createSphere(new Sphere(2.0), 20, 20);
        sphere.setCullFace(CullFace.NONE);

        root.getChildren().addAll(sphere);
        root.setTranslateX(scene.getWidth() / 2);
        root.setTranslateY(scene.getHeight() / 2);

        scene.setCamera(camera);

        primaryStage.setTitle("3D Viewer");
        primaryStage.setScene(scene);
        primaryStage.show();

        animate();
    }

    private void handleMousePressed(MouseEvent event) {
        mouseX = event.getSceneX();
        mouseY = event.getSceneY();
    }

    private void handleMouseDragged(MouseEvent event) {
        double deltaX = event.getSceneX() - mouseX;
        double deltaY = event.getSceneY() - mouseY;

        camYaw -= deltaX * MOUSE_SPEED;
        camPitch += deltaY * MOUSE_SPEED;

        camera.getTransforms().clear();
        camera.getTransforms().add(new Rotate(-camYaw, Rotate.Y_AXIS));
        camera.getTransforms().add(new Rotate(-camPitch, Rotate.X_AXIS));

        mouseX = event.getSceneX();
        mouseY = event.getSceneY();
    }

    private void handleKeyPressed(KeyEvent event) {
        switch (event.getCode()) {
            case UP:
                camera.setTranslateZ(camera.getTranslateZ() + CAM_SPEED);
                break;
            case DOWN:
                camera.setTranslateZ(camera.getTranslateZ() - CAM_SPEED);
                break;
        }
    }

    private void animate() {
        sphere.setRotationAxis(Rotate.Y_AXIS);
        sphere.setRotate(sphere.getRotate() + ROTATION_SPEED);
    }

    private Sphere createSphere(Sphere sphere, int slices, int stacks) {
        Mesh mesh = sphere.getMesh();
        int vertexCount = mesh.getPointElementSize() / 3;

        for (int i = 0; i < vertexCount; i++) {
            float x = (float) mesh.getPointElement(i * 3);
            float y = (float) mesh.getPointElement(i * 3 + 1);
            float z = (float) mesh.getPointElement(i * 3 + 2);

            double longitude = 2.0 * i / (slices - 1) * Math.PI;
            double latitude = 0.0;

            for (int j = 0; j < stacks; j++) {
                latitude = j / (double) (stacks - 1) * Math.PI - 0.5 * Math.PI;
                double newX = x * Math.sin(longitude) * Math.cos(latitude);
                double newY = y * Math.sin(longitude) * Math.sin(latitude);
                double newZ = z * -Math.cos(longitude);

                mesh.getPoints().addAll(newX, newY, newZ);
            }
        }

        return sphere;
    }

    public static void main(String[] args) {
        launch(args);
    }
}
