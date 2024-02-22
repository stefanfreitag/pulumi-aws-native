// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rekognition

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::Rekognition::StreamProcessor type is used to create an Amazon Rekognition StreamProcessor that you can use to analyze streaming videos.
type StreamProcessor struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.
	BoundingBoxRegionsOfInterest StreamProcessorBoundingBoxArrayOutput         `pulumi:"boundingBoxRegionsOfInterest"`
	ConnectedHomeSettings        StreamProcessorConnectedHomeSettingsPtrOutput `pulumi:"connectedHomeSettings"`
	DataSharingPreference        StreamProcessorDataSharingPreferencePtrOutput `pulumi:"dataSharingPreference"`
	FaceSearchSettings           StreamProcessorFaceSearchSettingsPtrOutput    `pulumi:"faceSearchSettings"`
	KinesisDataStream            StreamProcessorKinesisDataStreamPtrOutput     `pulumi:"kinesisDataStream"`
	KinesisVideoStream           StreamProcessorKinesisVideoStreamOutput       `pulumi:"kinesisVideoStream"`
	// The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.
	KmsKeyId pulumi.StringPtrOutput `pulumi:"kmsKeyId"`
	// Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.
	Name                pulumi.StringPtrOutput                      `pulumi:"name"`
	NotificationChannel StreamProcessorNotificationChannelPtrOutput `pulumi:"notificationChannel"`
	// The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point
	PolygonRegionsOfInterest StreamProcessorPointArrayArrayOutput `pulumi:"polygonRegionsOfInterest"`
	// ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.
	RoleArn       pulumi.StringOutput                   `pulumi:"roleArn"`
	S3Destination StreamProcessorS3DestinationPtrOutput `pulumi:"s3Destination"`
	// Current status of the stream processor.
	Status pulumi.StringOutput `pulumi:"status"`
	// Detailed status message about the stream processor.
	StatusMessage pulumi.StringOutput `pulumi:"statusMessage"`
	// An array of key-value pairs to apply to this resource.
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewStreamProcessor registers a new resource with the given unique name, arguments, and options.
func NewStreamProcessor(ctx *pulumi.Context,
	name string, args *StreamProcessorArgs, opts ...pulumi.ResourceOption) (*StreamProcessor, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.KinesisVideoStream == nil {
		return nil, errors.New("invalid value for required argument 'KinesisVideoStream'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"boundingBoxRegionsOfInterest[*]",
		"connectedHomeSettings",
		"dataSharingPreference",
		"faceSearchSettings",
		"kinesisDataStream",
		"kinesisVideoStream",
		"kmsKeyId",
		"name",
		"notificationChannel",
		"polygonRegionsOfInterest[*]",
		"roleArn",
		"s3Destination",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource StreamProcessor
	err := ctx.RegisterResource("aws-native:rekognition:StreamProcessor", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStreamProcessor gets an existing StreamProcessor resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStreamProcessor(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StreamProcessorState, opts ...pulumi.ResourceOption) (*StreamProcessor, error) {
	var resource StreamProcessor
	err := ctx.ReadResource("aws-native:rekognition:StreamProcessor", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StreamProcessor resources.
type streamProcessorState struct {
}

type StreamProcessorState struct {
}

func (StreamProcessorState) ElementType() reflect.Type {
	return reflect.TypeOf((*streamProcessorState)(nil)).Elem()
}

type streamProcessorArgs struct {
	// The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.
	BoundingBoxRegionsOfInterest []StreamProcessorBoundingBox          `pulumi:"boundingBoxRegionsOfInterest"`
	ConnectedHomeSettings        *StreamProcessorConnectedHomeSettings `pulumi:"connectedHomeSettings"`
	DataSharingPreference        *StreamProcessorDataSharingPreference `pulumi:"dataSharingPreference"`
	FaceSearchSettings           *StreamProcessorFaceSearchSettings    `pulumi:"faceSearchSettings"`
	KinesisDataStream            *StreamProcessorKinesisDataStream     `pulumi:"kinesisDataStream"`
	KinesisVideoStream           StreamProcessorKinesisVideoStream     `pulumi:"kinesisVideoStream"`
	// The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.
	Name                *string                             `pulumi:"name"`
	NotificationChannel *StreamProcessorNotificationChannel `pulumi:"notificationChannel"`
	// The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point
	PolygonRegionsOfInterest [][]StreamProcessorPoint `pulumi:"polygonRegionsOfInterest"`
	// ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.
	RoleArn       string                        `pulumi:"roleArn"`
	S3Destination *StreamProcessorS3Destination `pulumi:"s3Destination"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a StreamProcessor resource.
type StreamProcessorArgs struct {
	// The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.
	BoundingBoxRegionsOfInterest StreamProcessorBoundingBoxArrayInput
	ConnectedHomeSettings        StreamProcessorConnectedHomeSettingsPtrInput
	DataSharingPreference        StreamProcessorDataSharingPreferencePtrInput
	FaceSearchSettings           StreamProcessorFaceSearchSettingsPtrInput
	KinesisDataStream            StreamProcessorKinesisDataStreamPtrInput
	KinesisVideoStream           StreamProcessorKinesisVideoStreamInput
	// The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.
	KmsKeyId pulumi.StringPtrInput
	// Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.
	Name                pulumi.StringPtrInput
	NotificationChannel StreamProcessorNotificationChannelPtrInput
	// The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point
	PolygonRegionsOfInterest StreamProcessorPointArrayArrayInput
	// ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.
	RoleArn       pulumi.StringInput
	S3Destination StreamProcessorS3DestinationPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags aws.TagArrayInput
}

func (StreamProcessorArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*streamProcessorArgs)(nil)).Elem()
}

type StreamProcessorInput interface {
	pulumi.Input

	ToStreamProcessorOutput() StreamProcessorOutput
	ToStreamProcessorOutputWithContext(ctx context.Context) StreamProcessorOutput
}

func (*StreamProcessor) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamProcessor)(nil)).Elem()
}

func (i *StreamProcessor) ToStreamProcessorOutput() StreamProcessorOutput {
	return i.ToStreamProcessorOutputWithContext(context.Background())
}

func (i *StreamProcessor) ToStreamProcessorOutputWithContext(ctx context.Context) StreamProcessorOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StreamProcessorOutput)
}

type StreamProcessorOutput struct{ *pulumi.OutputState }

func (StreamProcessorOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StreamProcessor)(nil)).Elem()
}

func (o StreamProcessorOutput) ToStreamProcessorOutput() StreamProcessorOutput {
	return o
}

func (o StreamProcessorOutput) ToStreamProcessorOutputWithContext(ctx context.Context) StreamProcessorOutput {
	return o
}

func (o StreamProcessorOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamProcessor) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.
func (o StreamProcessorOutput) BoundingBoxRegionsOfInterest() StreamProcessorBoundingBoxArrayOutput {
	return o.ApplyT(func(v *StreamProcessor) StreamProcessorBoundingBoxArrayOutput { return v.BoundingBoxRegionsOfInterest }).(StreamProcessorBoundingBoxArrayOutput)
}

func (o StreamProcessorOutput) ConnectedHomeSettings() StreamProcessorConnectedHomeSettingsPtrOutput {
	return o.ApplyT(func(v *StreamProcessor) StreamProcessorConnectedHomeSettingsPtrOutput { return v.ConnectedHomeSettings }).(StreamProcessorConnectedHomeSettingsPtrOutput)
}

func (o StreamProcessorOutput) DataSharingPreference() StreamProcessorDataSharingPreferencePtrOutput {
	return o.ApplyT(func(v *StreamProcessor) StreamProcessorDataSharingPreferencePtrOutput { return v.DataSharingPreference }).(StreamProcessorDataSharingPreferencePtrOutput)
}

func (o StreamProcessorOutput) FaceSearchSettings() StreamProcessorFaceSearchSettingsPtrOutput {
	return o.ApplyT(func(v *StreamProcessor) StreamProcessorFaceSearchSettingsPtrOutput { return v.FaceSearchSettings }).(StreamProcessorFaceSearchSettingsPtrOutput)
}

func (o StreamProcessorOutput) KinesisDataStream() StreamProcessorKinesisDataStreamPtrOutput {
	return o.ApplyT(func(v *StreamProcessor) StreamProcessorKinesisDataStreamPtrOutput { return v.KinesisDataStream }).(StreamProcessorKinesisDataStreamPtrOutput)
}

func (o StreamProcessorOutput) KinesisVideoStream() StreamProcessorKinesisVideoStreamOutput {
	return o.ApplyT(func(v *StreamProcessor) StreamProcessorKinesisVideoStreamOutput { return v.KinesisVideoStream }).(StreamProcessorKinesisVideoStreamOutput)
}

// The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.
func (o StreamProcessorOutput) KmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StreamProcessor) pulumi.StringPtrOutput { return v.KmsKeyId }).(pulumi.StringPtrOutput)
}

// Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.
func (o StreamProcessorOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StreamProcessor) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o StreamProcessorOutput) NotificationChannel() StreamProcessorNotificationChannelPtrOutput {
	return o.ApplyT(func(v *StreamProcessor) StreamProcessorNotificationChannelPtrOutput { return v.NotificationChannel }).(StreamProcessorNotificationChannelPtrOutput)
}

// The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point
func (o StreamProcessorOutput) PolygonRegionsOfInterest() StreamProcessorPointArrayArrayOutput {
	return o.ApplyT(func(v *StreamProcessor) StreamProcessorPointArrayArrayOutput { return v.PolygonRegionsOfInterest }).(StreamProcessorPointArrayArrayOutput)
}

// ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.
func (o StreamProcessorOutput) RoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamProcessor) pulumi.StringOutput { return v.RoleArn }).(pulumi.StringOutput)
}

func (o StreamProcessorOutput) S3Destination() StreamProcessorS3DestinationPtrOutput {
	return o.ApplyT(func(v *StreamProcessor) StreamProcessorS3DestinationPtrOutput { return v.S3Destination }).(StreamProcessorS3DestinationPtrOutput)
}

// Current status of the stream processor.
func (o StreamProcessorOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamProcessor) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// Detailed status message about the stream processor.
func (o StreamProcessorOutput) StatusMessage() pulumi.StringOutput {
	return o.ApplyT(func(v *StreamProcessor) pulumi.StringOutput { return v.StatusMessage }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o StreamProcessorOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *StreamProcessor) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StreamProcessorInput)(nil)).Elem(), &StreamProcessor{})
	pulumi.RegisterOutputType(StreamProcessorOutput{})
}
