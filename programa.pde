/*
Thomas Sanchez Lengeling.
 http://codigogenerativo.com/
 
 KinectPV2, Kinect for Windows v2 library for processing
 
 Skeleton color map example.
 Skeleton (x,y) positions are mapped to match the color Frame
 */
/*
 GoToLoop
 https://forum.processing.org/two/discussion/20305/saving-data-variables-in-processing.html
 * Save Coords Table (v1.0)
 * GoToLoop (2017-Jan-17)
 *
 * forum.Processing.org/two/discussion/20305/
 * saving-data-variables-in-processing#Item_17
 */
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 PROYECTO DE TÍTULO 2022
 DISEÑO DE INTERACCIÓN DIGITAL
 SISTEMA DE APOYO AL ENTRENAMIENTO DE TIRO CON ARCO
 VALERIA MIRANDA FIGUEROA
 */
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


//Importe de librería KinectPV2
import KinectPV2.KJoint;
import KinectPV2.*;
import processing.data.*;

KinectPV2 kinect; 


//DELIMITACIONES DE ALINEACIÓN CON EL HOMBRO IZQUIERDO COMO BASE DE REFERENCIA 
//Aquí delimité el hombro como referencia de posición base, así le agregué rangos de posición a otras partes del cuerpo según el hombro

//EJE Y
//Mano arco
int offset1MA = 10;
int offset2MA = 100;
//Mano cuerda
int offset1MC = 10;
int offset2MC = 100;
//Codo
int offset1Codo = 10;
int offset2Codo = 100;

//EJE X
//Mano cuerda
//Armado (Preparación)
int offset1MCxP = -400;
int offset2MCxP = -70;
//Anclaje
int offset1MCxA = 120;
int offset2MCxA = -70;
//Liberación
int offset1MCxL = 300;
int offset2MCxL = -120;

//TEXTO
//Tamaño texto en pantalla
int TT = 30;


////--------------------
//Establecimiento de la tabla y sus títulos/variables
String[] HEADER = { "ManoCuerdaX", "CodoX", "ManoCuerdaY", "CodoY"};
String FILENAME = "A.csv";

Table coords;
Object[] vvv = new Object[HEADER.length];
float ManoCuerdaX, CodoX, ManoCuerdaY, CodoY, ManoCuerdaXX, ManoCuerdaYY; 
////--------------------

void setup() {
  size(1920, 1080, P3D); //canvas

  kinect = new KinectPV2(this);

  kinect.enableSkeletonColorMap(true);
  kinect.enableColorImg(true);

  kinect.init();

  ////-------------------
  coords = new Table();
  coords.setColumnTitles(HEADER);
  coords.setTableType("float");
  ////-------------------
  //frameRate (5);
}

void draw() {
  background(0);
  
  image(kinect.getColorImage(), 0, 0, width, height);

  ////-------------------

  ArrayList<KSkeleton> skeletonArray =  kinect.getSkeletonColorMap();

  //individual JOINTS
  for (int i = 0; i < skeletonArray.size(); i++) {
    KSkeleton skeleton = (KSkeleton) skeletonArray.get(i);
    if (skeleton.isTracked()) {
      KJoint[] joints = skeleton.getJoints();

      color col  = skeleton.getIndexColor();
      fill(col);
      stroke(col);
      drawBody(joints);

      //draw different color for each hand state
      drawHandState(joints[KinectPV2.JointType_HandRight]); 
      drawHandState(joints[KinectPV2.JointType_HandLeft]);

      ManoCuerdaX = joints[KinectPV2.JointType_HandRight].getX();
      CodoX = joints[KinectPV2.JointType_ElbowRight].getX();
      
      ManoCuerdaXX = joints[KinectPV2.JointType_HandLeft].getX();
      ManoCuerdaYY = joints[KinectPV2.JointType_HandLeft].getY();

      ManoCuerdaY = joints[KinectPV2.JointType_HandRight].getY();
      CodoY = joints[KinectPV2.JointType_ElbowRight].getY();

    }
  } 
  String[] mensajes = {str(ManoCuerdaX), str(ManoCuerdaY),str(ManoCuerdaXX),str(ManoCuerdaYY)};
  saveStrings("actualiza.txt", mensajes);
  fill(255, 0, 0);
  text(frameRate, 50, 50);
  fill(255, 0, 0);
  ellipse(ManoCuerdaX,ManoCuerdaY, 40, 40);
  fill(255, 0, 0);
  ellipse(ManoCuerdaXX,ManoCuerdaYY, 40, 40);
}

////-------------------
void addNewCoordRow() {
  vvv[0] = ManoCuerdaX;
  vvv[1] = CodoX;
  vvv[2] = ManoCuerdaY;
  vvv[3] = CodoY;
  coords.addRow(vvv);
}
////-------------------

//DRAW BODY
void drawBody(KJoint[] joints) { //HUESOS DE CONEXIÓN ENTRE ARTICULACIONES
  drawBone(joints, KinectPV2.JointType_Head, KinectPV2.JointType_Neck); 
  drawBone(joints, KinectPV2.JointType_Neck, KinectPV2.JointType_SpineShoulder); 
  drawBone(joints, KinectPV2.JointType_SpineShoulder, KinectPV2.JointType_SpineMid);
  drawBone(joints, KinectPV2.JointType_SpineMid, KinectPV2.JointType_SpineBase);
  drawBone(joints, KinectPV2.JointType_SpineShoulder, KinectPV2.JointType_ShoulderRight);
  drawBone(joints, KinectPV2.JointType_SpineShoulder, KinectPV2.JointType_ShoulderLeft);
  drawBone(joints, KinectPV2.JointType_SpineBase, KinectPV2.JointType_HipRight);
  drawBone(joints, KinectPV2.JointType_SpineBase, KinectPV2.JointType_HipLeft);

  // Right Arm
  //SUPERIOR DERECHO
  drawBone(joints, KinectPV2.JointType_ShoulderRight, KinectPV2.JointType_ElbowRight);
  drawBone(joints, KinectPV2.JointType_ElbowRight, KinectPV2.JointType_WristRight);
  drawBone(joints, KinectPV2.JointType_WristRight, KinectPV2.JointType_HandRight);
  drawBone(joints, KinectPV2.JointType_HandRight, KinectPV2.JointType_HandTipRight);
  drawBone(joints, KinectPV2.JointType_WristRight, KinectPV2.JointType_ThumbRight);

  // Left Arm
  //SUPERIOR IZQUIERDO
  drawBone(joints, KinectPV2.JointType_ShoulderLeft, KinectPV2.JointType_ElbowLeft);
  drawBone(joints, KinectPV2.JointType_ElbowLeft, KinectPV2.JointType_WristLeft);
  drawBone(joints, KinectPV2.JointType_WristLeft, KinectPV2.JointType_HandLeft);
  drawBone(joints, KinectPV2.JointType_HandLeft, KinectPV2.JointType_HandTipLeft);
  drawBone(joints, KinectPV2.JointType_WristLeft, KinectPV2.JointType_ThumbLeft);

  // Right Leg
  //INFERIOR DERECHO
  drawBone(joints, KinectPV2.JointType_HipRight, KinectPV2.JointType_KneeRight);
  drawBone(joints, KinectPV2.JointType_KneeRight, KinectPV2.JointType_AnkleRight);
  drawBone(joints, KinectPV2.JointType_AnkleRight, KinectPV2.JointType_FootRight);

  // Left Leg
  //INFERIOR IZQUIERDO
  drawBone(joints, KinectPV2.JointType_HipLeft, KinectPV2.JointType_KneeLeft);
  drawBone(joints, KinectPV2.JointType_KneeLeft, KinectPV2.JointType_AnkleLeft);
  drawBone(joints, KinectPV2.JointType_AnkleLeft, KinectPV2.JointType_FootLeft);

  //ARTICULACIONES, punta de las manos y pies
  drawJoint(joints, KinectPV2.JointType_HandTipLeft);
  drawJoint(joints, KinectPV2.JointType_HandTipRight);
  drawJoint(joints, KinectPV2.JointType_FootLeft);
  drawJoint(joints, KinectPV2.JointType_FootRight);

  //ARTICULACIÓN PULGARES
  drawJoint(joints, KinectPV2.JointType_ThumbLeft);
  drawJoint(joints, KinectPV2.JointType_ThumbRight);

  //CABEZA
  drawJoint(joints, KinectPV2.JointType_Head);
}

//draw joint
void drawJoint(KJoint[] joints, int jointType) {
  pushMatrix();
  //translate(joints[jointType].getX(), joints[jointType].getY(), joints[jointType].getZ());
  ellipse(joints[jointType].getX(), joints[jointType].getY(), 25, 25);
  popMatrix();
}

//draw bone
void drawBone(KJoint[] joints, int jointType1, int jointType2) {
  pushMatrix();
  translate(joints[jointType1].getX(), joints[jointType1].getY(), joints[jointType1].getZ());
  ellipse(0, 0, 25, 25);
  popMatrix();
  line(joints[jointType1].getX(), joints[jointType1].getY(), joints[jointType1].getZ(), joints[jointType2].getX(), joints[jointType2].getY(), joints[jointType2].getZ());
}

//draw hand state
//ESTADO DE LA MANO, abierta, cerrada, pulgar
void drawHandState(KJoint joint) {
  noStroke();
  handState(joint.getState());
  pushMatrix();
  translate(joint.getX(), joint.getY(), joint.getZ());
  ellipse(0, 0, 70, 70);
  popMatrix();
}

/*
Different hand state
 KinectPV2.HandState_Open
 KinectPV2.HandState_Closed
 KinectPV2.HandState_Lasso
 KinectPV2.HandState_NotTracked
 */

void handState(int handState) {
  switch(handState) {
  case KinectPV2.HandState_Open:
    fill(0, 255, 0); // VERDE CUANDO LA MANO ESTÁ ABIERTA
    break;
  case KinectPV2.HandState_Closed:
    fill(255, 0, 0); //ROJO CUANDO LA MANO ESTÁ CERRADA
    
    break;
  case KinectPV2.HandState_Lasso:
    fill(0, 0, 255); // AZUL - INDICACIÓN CON 1 DEDO
    break;
  case KinectPV2.HandState_NotTracked:
    fill(255, 255, 255); //BLANCO CUANDO NO DETECTA SU ESTADO
    break;
  }
}
