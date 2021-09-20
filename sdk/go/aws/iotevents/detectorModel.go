// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iotevents

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.
type DetectorModel struct {
	pulumi.CustomResourceState

	DetectorModelDefinition DetectorModelDetectorModelDefinitionOutput `pulumi:"detectorModelDefinition"`
	// A brief description of the detector model.
	DetectorModelDescription pulumi.StringPtrOutput `pulumi:"detectorModelDescription"`
	// The name of the detector model.
	DetectorModelName pulumi.StringPtrOutput `pulumi:"detectorModelName"`
	// Information about the order in which events are evaluated and how actions are executed.
	EvaluationMethod DetectorModelEvaluationMethodPtrOutput `pulumi:"evaluationMethod"`
	// The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.
	//
	// This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.
	Key pulumi.StringPtrOutput `pulumi:"key"`
	// The ARN of the role that grants permission to AWS IoT Events to perform its operations.
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// An array of key-value pairs to apply to this resource.
	//
	// For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
	Tags DetectorModelTagArrayOutput `pulumi:"tags"`
}

// NewDetectorModel registers a new resource with the given unique name, arguments, and options.
func NewDetectorModel(ctx *pulumi.Context,
	name string, args *DetectorModelArgs, opts ...pulumi.ResourceOption) (*DetectorModel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DetectorModelDefinition == nil {
		return nil, errors.New("invalid value for required argument 'DetectorModelDefinition'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource DetectorModel
	err := ctx.RegisterResource("aws-native:iotevents:DetectorModel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDetectorModel gets an existing DetectorModel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDetectorModel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DetectorModelState, opts ...pulumi.ResourceOption) (*DetectorModel, error) {
	var resource DetectorModel
	err := ctx.ReadResource("aws-native:iotevents:DetectorModel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DetectorModel resources.
type detectorModelState struct {
}

type DetectorModelState struct {
}

func (DetectorModelState) ElementType() reflect.Type {
	return reflect.TypeOf((*detectorModelState)(nil)).Elem()
}

type detectorModelArgs struct {
	DetectorModelDefinition DetectorModelDetectorModelDefinition `pulumi:"detectorModelDefinition"`
	// A brief description of the detector model.
	DetectorModelDescription *string `pulumi:"detectorModelDescription"`
	// The name of the detector model.
	DetectorModelName *string `pulumi:"detectorModelName"`
	// Information about the order in which events are evaluated and how actions are executed.
	EvaluationMethod *DetectorModelEvaluationMethod `pulumi:"evaluationMethod"`
	// The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.
	//
	// This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.
	Key *string `pulumi:"key"`
	// The ARN of the role that grants permission to AWS IoT Events to perform its operations.
	RoleArn string `pulumi:"roleArn"`
	// An array of key-value pairs to apply to this resource.
	//
	// For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
	Tags []DetectorModelTag `pulumi:"tags"`
}

// The set of arguments for constructing a DetectorModel resource.
type DetectorModelArgs struct {
	DetectorModelDefinition DetectorModelDetectorModelDefinitionInput
	// A brief description of the detector model.
	DetectorModelDescription pulumi.StringPtrInput
	// The name of the detector model.
	DetectorModelName pulumi.StringPtrInput
	// Information about the order in which events are evaluated and how actions are executed.
	EvaluationMethod DetectorModelEvaluationMethodPtrInput
	// The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.
	//
	// This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.
	Key pulumi.StringPtrInput
	// The ARN of the role that grants permission to AWS IoT Events to perform its operations.
	RoleArn pulumi.StringInput
	// An array of key-value pairs to apply to this resource.
	//
	// For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
	Tags DetectorModelTagArrayInput
}

func (DetectorModelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*detectorModelArgs)(nil)).Elem()
}

type DetectorModelInput interface {
	pulumi.Input

	ToDetectorModelOutput() DetectorModelOutput
	ToDetectorModelOutputWithContext(ctx context.Context) DetectorModelOutput
}

func (*DetectorModel) ElementType() reflect.Type {
	return reflect.TypeOf((*DetectorModel)(nil))
}

func (i *DetectorModel) ToDetectorModelOutput() DetectorModelOutput {
	return i.ToDetectorModelOutputWithContext(context.Background())
}

func (i *DetectorModel) ToDetectorModelOutputWithContext(ctx context.Context) DetectorModelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DetectorModelOutput)
}

type DetectorModelOutput struct{ *pulumi.OutputState }

func (DetectorModelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DetectorModel)(nil))
}

func (o DetectorModelOutput) ToDetectorModelOutput() DetectorModelOutput {
	return o
}

func (o DetectorModelOutput) ToDetectorModelOutputWithContext(ctx context.Context) DetectorModelOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DetectorModelOutput{})
}
