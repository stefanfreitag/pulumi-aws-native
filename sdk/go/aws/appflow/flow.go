// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appflow

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::AppFlow::Flow.
type Flow struct {
	pulumi.CustomResourceState

	// Description of the flow.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// List of Destination connectors of the flow.
	DestinationFlowConfigList FlowDestinationFlowConfigArrayOutput `pulumi:"destinationFlowConfigList"`
	// ARN identifier of the flow.
	FlowArn pulumi.StringOutput `pulumi:"flowArn"`
	// Name of the flow.
	FlowName pulumi.StringOutput `pulumi:"flowName"`
	// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
	KMSArn pulumi.StringPtrOutput `pulumi:"kMSArn"`
	// Configurations of Source connector of the flow.
	SourceFlowConfig FlowSourceFlowConfigOutput `pulumi:"sourceFlowConfig"`
	// List of Tags.
	Tags FlowTagArrayOutput `pulumi:"tags"`
	// List of tasks for the flow.
	Tasks FlowTaskArrayOutput `pulumi:"tasks"`
	// Trigger settings of the flow.
	TriggerConfig FlowTriggerConfigOutput `pulumi:"triggerConfig"`
}

// NewFlow registers a new resource with the given unique name, arguments, and options.
func NewFlow(ctx *pulumi.Context,
	name string, args *FlowArgs, opts ...pulumi.ResourceOption) (*Flow, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DestinationFlowConfigList == nil {
		return nil, errors.New("invalid value for required argument 'DestinationFlowConfigList'")
	}
	if args.FlowName == nil {
		return nil, errors.New("invalid value for required argument 'FlowName'")
	}
	if args.SourceFlowConfig == nil {
		return nil, errors.New("invalid value for required argument 'SourceFlowConfig'")
	}
	if args.Tasks == nil {
		return nil, errors.New("invalid value for required argument 'Tasks'")
	}
	if args.TriggerConfig == nil {
		return nil, errors.New("invalid value for required argument 'TriggerConfig'")
	}
	var resource Flow
	err := ctx.RegisterResource("aws-native:appflow:Flow", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFlow gets an existing Flow resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFlow(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FlowState, opts ...pulumi.ResourceOption) (*Flow, error) {
	var resource Flow
	err := ctx.ReadResource("aws-native:appflow:Flow", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Flow resources.
type flowState struct {
}

type FlowState struct {
}

func (FlowState) ElementType() reflect.Type {
	return reflect.TypeOf((*flowState)(nil)).Elem()
}

type flowArgs struct {
	// Description of the flow.
	Description *string `pulumi:"description"`
	// List of Destination connectors of the flow.
	DestinationFlowConfigList []FlowDestinationFlowConfig `pulumi:"destinationFlowConfigList"`
	// Name of the flow.
	FlowName string `pulumi:"flowName"`
	// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
	KMSArn *string `pulumi:"kMSArn"`
	// Configurations of Source connector of the flow.
	SourceFlowConfig FlowSourceFlowConfig `pulumi:"sourceFlowConfig"`
	// List of Tags.
	Tags []FlowTag `pulumi:"tags"`
	// List of tasks for the flow.
	Tasks []FlowTask `pulumi:"tasks"`
	// Trigger settings of the flow.
	TriggerConfig FlowTriggerConfig `pulumi:"triggerConfig"`
}

// The set of arguments for constructing a Flow resource.
type FlowArgs struct {
	// Description of the flow.
	Description pulumi.StringPtrInput
	// List of Destination connectors of the flow.
	DestinationFlowConfigList FlowDestinationFlowConfigArrayInput
	// Name of the flow.
	FlowName pulumi.StringInput
	// The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
	KMSArn pulumi.StringPtrInput
	// Configurations of Source connector of the flow.
	SourceFlowConfig FlowSourceFlowConfigInput
	// List of Tags.
	Tags FlowTagArrayInput
	// List of tasks for the flow.
	Tasks FlowTaskArrayInput
	// Trigger settings of the flow.
	TriggerConfig FlowTriggerConfigInput
}

func (FlowArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*flowArgs)(nil)).Elem()
}

type FlowInput interface {
	pulumi.Input

	ToFlowOutput() FlowOutput
	ToFlowOutputWithContext(ctx context.Context) FlowOutput
}

func (*Flow) ElementType() reflect.Type {
	return reflect.TypeOf((*Flow)(nil))
}

func (i *Flow) ToFlowOutput() FlowOutput {
	return i.ToFlowOutputWithContext(context.Background())
}

func (i *Flow) ToFlowOutputWithContext(ctx context.Context) FlowOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FlowOutput)
}

type FlowOutput struct{ *pulumi.OutputState }

func (FlowOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Flow)(nil))
}

func (o FlowOutput) ToFlowOutput() FlowOutput {
	return o
}

func (o FlowOutput) ToFlowOutputWithContext(ctx context.Context) FlowOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(FlowOutput{})
}
