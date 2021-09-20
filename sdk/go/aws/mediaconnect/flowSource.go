// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mediaconnect

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::MediaConnect::FlowSource
type FlowSource struct {
	pulumi.CustomResourceState

	// The type of encryption that is used on the content ingested from this source.
	Decryption FlowSourceEncryptionPtrOutput `pulumi:"decryption"`
	// A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
	Description pulumi.StringOutput `pulumi:"description"`
	// The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.
	EntitlementArn pulumi.StringPtrOutput `pulumi:"entitlementArn"`
	// The ARN of the flow.
	FlowArn pulumi.StringPtrOutput `pulumi:"flowArn"`
	// The IP address that the flow will be listening on for incoming content.
	IngestIp pulumi.StringOutput `pulumi:"ingestIp"`
	// The port that the flow will be listening on for incoming content.
	IngestPort pulumi.IntPtrOutput `pulumi:"ingestPort"`
	// The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
	MaxBitrate pulumi.IntPtrOutput `pulumi:"maxBitrate"`
	// The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
	MaxLatency pulumi.IntPtrOutput `pulumi:"maxLatency"`
	// The name of the source.
	Name pulumi.StringOutput `pulumi:"name"`
	// The protocol that is used by the source.
	Protocol FlowSourceProtocolPtrOutput `pulumi:"protocol"`
	// The ARN of the source.
	SourceArn pulumi.StringOutput `pulumi:"sourceArn"`
	// The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
	StreamId pulumi.StringPtrOutput `pulumi:"streamId"`
	// The name of the VPC Interface this Source is configured with.
	VpcInterfaceName pulumi.StringPtrOutput `pulumi:"vpcInterfaceName"`
	// The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
	WhitelistCidr pulumi.StringPtrOutput `pulumi:"whitelistCidr"`
}

// NewFlowSource registers a new resource with the given unique name, arguments, and options.
func NewFlowSource(ctx *pulumi.Context,
	name string, args *FlowSourceArgs, opts ...pulumi.ResourceOption) (*FlowSource, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource FlowSource
	err := ctx.RegisterResource("aws-native:mediaconnect:FlowSource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFlowSource gets an existing FlowSource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFlowSource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FlowSourceState, opts ...pulumi.ResourceOption) (*FlowSource, error) {
	var resource FlowSource
	err := ctx.ReadResource("aws-native:mediaconnect:FlowSource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FlowSource resources.
type flowSourceState struct {
}

type FlowSourceState struct {
}

func (FlowSourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*flowSourceState)(nil)).Elem()
}

type flowSourceArgs struct {
	// The type of encryption that is used on the content ingested from this source.
	Decryption *FlowSourceEncryption `pulumi:"decryption"`
	// A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
	Description string `pulumi:"description"`
	// The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.
	EntitlementArn *string `pulumi:"entitlementArn"`
	// The ARN of the flow.
	FlowArn *string `pulumi:"flowArn"`
	// The port that the flow will be listening on for incoming content.
	IngestPort *int `pulumi:"ingestPort"`
	// The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
	MaxBitrate *int `pulumi:"maxBitrate"`
	// The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
	MaxLatency *int `pulumi:"maxLatency"`
	// The name of the source.
	Name string `pulumi:"name"`
	// The protocol that is used by the source.
	Protocol *FlowSourceProtocol `pulumi:"protocol"`
	// The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
	StreamId *string `pulumi:"streamId"`
	// The name of the VPC Interface this Source is configured with.
	VpcInterfaceName *string `pulumi:"vpcInterfaceName"`
	// The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
	WhitelistCidr *string `pulumi:"whitelistCidr"`
}

// The set of arguments for constructing a FlowSource resource.
type FlowSourceArgs struct {
	// The type of encryption that is used on the content ingested from this source.
	Decryption FlowSourceEncryptionPtrInput
	// A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
	Description pulumi.StringInput
	// The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.
	EntitlementArn pulumi.StringPtrInput
	// The ARN of the flow.
	FlowArn pulumi.StringPtrInput
	// The port that the flow will be listening on for incoming content.
	IngestPort pulumi.IntPtrInput
	// The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
	MaxBitrate pulumi.IntPtrInput
	// The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
	MaxLatency pulumi.IntPtrInput
	// The name of the source.
	Name pulumi.StringInput
	// The protocol that is used by the source.
	Protocol FlowSourceProtocolPtrInput
	// The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
	StreamId pulumi.StringPtrInput
	// The name of the VPC Interface this Source is configured with.
	VpcInterfaceName pulumi.StringPtrInput
	// The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
	WhitelistCidr pulumi.StringPtrInput
}

func (FlowSourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*flowSourceArgs)(nil)).Elem()
}

type FlowSourceInput interface {
	pulumi.Input

	ToFlowSourceOutput() FlowSourceOutput
	ToFlowSourceOutputWithContext(ctx context.Context) FlowSourceOutput
}

func (*FlowSource) ElementType() reflect.Type {
	return reflect.TypeOf((*FlowSource)(nil))
}

func (i *FlowSource) ToFlowSourceOutput() FlowSourceOutput {
	return i.ToFlowSourceOutputWithContext(context.Background())
}

func (i *FlowSource) ToFlowSourceOutputWithContext(ctx context.Context) FlowSourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FlowSourceOutput)
}

type FlowSourceOutput struct{ *pulumi.OutputState }

func (FlowSourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FlowSource)(nil))
}

func (o FlowSourceOutput) ToFlowSourceOutput() FlowSourceOutput {
	return o
}

func (o FlowSourceOutput) ToFlowSourceOutputWithContext(ctx context.Context) FlowSourceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(FlowSourceOutput{})
}
