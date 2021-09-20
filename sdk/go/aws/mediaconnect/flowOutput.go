// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mediaconnect

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::MediaConnect::FlowOutput
type FlowOutput struct {
	pulumi.CustomResourceState

	// The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
	CidrAllowList pulumi.StringArrayOutput `pulumi:"cidrAllowList"`
	// A description of the output.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The address where you want to send the output.
	Destination pulumi.StringPtrOutput `pulumi:"destination"`
	// The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
	Encryption FlowOutputEncryptionPtrOutput `pulumi:"encryption"`
	// The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
	FlowArn pulumi.StringOutput `pulumi:"flowArn"`
	// The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
	MaxLatency pulumi.IntPtrOutput `pulumi:"maxLatency"`
	// The name of the output. This value must be unique within the current flow.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// The ARN of the output.
	OutputArn pulumi.StringOutput `pulumi:"outputArn"`
	// The port to use when content is distributed to this output.
	Port pulumi.IntPtrOutput `pulumi:"port"`
	// The protocol that is used by the source or output.
	Protocol FlowOutputProtocolOutput `pulumi:"protocol"`
	// The remote ID for the Zixi-pull stream.
	RemoteId pulumi.StringPtrOutput `pulumi:"remoteId"`
	// The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
	SmoothingLatency pulumi.IntPtrOutput `pulumi:"smoothingLatency"`
	// The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
	StreamId pulumi.StringPtrOutput `pulumi:"streamId"`
	// The name of the VPC interface attachment to use for this output.
	VpcInterfaceAttachment FlowOutputVpcInterfaceAttachmentPtrOutput `pulumi:"vpcInterfaceAttachment"`
}

// NewFlowOutput registers a new resource with the given unique name, arguments, and options.
func NewFlowOutput(ctx *pulumi.Context,
	name string, args *FlowOutputArgs, opts ...pulumi.ResourceOption) (*FlowOutput, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FlowArn == nil {
		return nil, errors.New("invalid value for required argument 'FlowArn'")
	}
	if args.Protocol == nil {
		return nil, errors.New("invalid value for required argument 'Protocol'")
	}
	var resource FlowOutput
	err := ctx.RegisterResource("aws-native:mediaconnect:FlowOutput", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFlowOutput gets an existing FlowOutput resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFlowOutput(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FlowOutputState, opts ...pulumi.ResourceOption) (*FlowOutput, error) {
	var resource FlowOutput
	err := ctx.ReadResource("aws-native:mediaconnect:FlowOutput", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FlowOutput resources.
type flowOutputState struct {
}

type FlowOutputState struct {
}

func (FlowOutputState) ElementType() reflect.Type {
	return reflect.TypeOf((*flowOutputState)(nil)).Elem()
}

type flowOutputArgs struct {
	// The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
	CidrAllowList []string `pulumi:"cidrAllowList"`
	// A description of the output.
	Description *string `pulumi:"description"`
	// The address where you want to send the output.
	Destination *string `pulumi:"destination"`
	// The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
	Encryption *FlowOutputEncryption `pulumi:"encryption"`
	// The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
	FlowArn string `pulumi:"flowArn"`
	// The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
	MaxLatency *int `pulumi:"maxLatency"`
	// The name of the output. This value must be unique within the current flow.
	Name *string `pulumi:"name"`
	// The port to use when content is distributed to this output.
	Port *int `pulumi:"port"`
	// The protocol that is used by the source or output.
	Protocol FlowOutputProtocol `pulumi:"protocol"`
	// The remote ID for the Zixi-pull stream.
	RemoteId *string `pulumi:"remoteId"`
	// The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
	SmoothingLatency *int `pulumi:"smoothingLatency"`
	// The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
	StreamId *string `pulumi:"streamId"`
	// The name of the VPC interface attachment to use for this output.
	VpcInterfaceAttachment *FlowOutputVpcInterfaceAttachment `pulumi:"vpcInterfaceAttachment"`
}

// The set of arguments for constructing a FlowOutput resource.
type FlowOutputArgs struct {
	// The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
	CidrAllowList pulumi.StringArrayInput
	// A description of the output.
	Description pulumi.StringPtrInput
	// The address where you want to send the output.
	Destination pulumi.StringPtrInput
	// The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
	Encryption FlowOutputEncryptionPtrInput
	// The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
	FlowArn pulumi.StringInput
	// The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
	MaxLatency pulumi.IntPtrInput
	// The name of the output. This value must be unique within the current flow.
	Name pulumi.StringPtrInput
	// The port to use when content is distributed to this output.
	Port pulumi.IntPtrInput
	// The protocol that is used by the source or output.
	Protocol FlowOutputProtocolInput
	// The remote ID for the Zixi-pull stream.
	RemoteId pulumi.StringPtrInput
	// The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
	SmoothingLatency pulumi.IntPtrInput
	// The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
	StreamId pulumi.StringPtrInput
	// The name of the VPC interface attachment to use for this output.
	VpcInterfaceAttachment FlowOutputVpcInterfaceAttachmentPtrInput
}

func (FlowOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*flowOutputArgs)(nil)).Elem()
}

type FlowOutputInput interface {
	pulumi.Input

	ToFlowOutputOutput() FlowOutputOutput
	ToFlowOutputOutputWithContext(ctx context.Context) FlowOutputOutput
}

func (*FlowOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FlowOutput)(nil))
}

func (i *FlowOutput) ToFlowOutputOutput() FlowOutputOutput {
	return i.ToFlowOutputOutputWithContext(context.Background())
}

func (i *FlowOutput) ToFlowOutputOutputWithContext(ctx context.Context) FlowOutputOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FlowOutputOutput)
}

type FlowOutputOutput struct{ *pulumi.OutputState }

func (FlowOutputOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FlowOutput)(nil))
}

func (o FlowOutputOutput) ToFlowOutputOutput() FlowOutputOutput {
	return o
}

func (o FlowOutputOutput) ToFlowOutputOutputWithContext(ctx context.Context) FlowOutputOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(FlowOutputOutput{})
}
