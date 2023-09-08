// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EC2::VPCEndpointConnectionNotification
//
// Deprecated: VpcEndpointConnectionNotification is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type VpcEndpointConnectionNotification struct {
	pulumi.CustomResourceState

	ConnectionEvents          pulumi.StringArrayOutput `pulumi:"connectionEvents"`
	ConnectionNotificationArn pulumi.StringOutput      `pulumi:"connectionNotificationArn"`
	ServiceId                 pulumi.StringPtrOutput   `pulumi:"serviceId"`
	VpcEndpointId             pulumi.StringPtrOutput   `pulumi:"vpcEndpointId"`
}

// NewVpcEndpointConnectionNotification registers a new resource with the given unique name, arguments, and options.
func NewVpcEndpointConnectionNotification(ctx *pulumi.Context,
	name string, args *VpcEndpointConnectionNotificationArgs, opts ...pulumi.ResourceOption) (*VpcEndpointConnectionNotification, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConnectionEvents == nil {
		return nil, errors.New("invalid value for required argument 'ConnectionEvents'")
	}
	if args.ConnectionNotificationArn == nil {
		return nil, errors.New("invalid value for required argument 'ConnectionNotificationArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"serviceId",
		"vpcEndpointId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VpcEndpointConnectionNotification
	err := ctx.RegisterResource("aws-native:ec2:VpcEndpointConnectionNotification", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpcEndpointConnectionNotification gets an existing VpcEndpointConnectionNotification resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcEndpointConnectionNotification(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpcEndpointConnectionNotificationState, opts ...pulumi.ResourceOption) (*VpcEndpointConnectionNotification, error) {
	var resource VpcEndpointConnectionNotification
	err := ctx.ReadResource("aws-native:ec2:VpcEndpointConnectionNotification", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpcEndpointConnectionNotification resources.
type vpcEndpointConnectionNotificationState struct {
}

type VpcEndpointConnectionNotificationState struct {
}

func (VpcEndpointConnectionNotificationState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcEndpointConnectionNotificationState)(nil)).Elem()
}

type vpcEndpointConnectionNotificationArgs struct {
	ConnectionEvents          []string `pulumi:"connectionEvents"`
	ConnectionNotificationArn string   `pulumi:"connectionNotificationArn"`
	ServiceId                 *string  `pulumi:"serviceId"`
	VpcEndpointId             *string  `pulumi:"vpcEndpointId"`
}

// The set of arguments for constructing a VpcEndpointConnectionNotification resource.
type VpcEndpointConnectionNotificationArgs struct {
	ConnectionEvents          pulumi.StringArrayInput
	ConnectionNotificationArn pulumi.StringInput
	ServiceId                 pulumi.StringPtrInput
	VpcEndpointId             pulumi.StringPtrInput
}

func (VpcEndpointConnectionNotificationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcEndpointConnectionNotificationArgs)(nil)).Elem()
}

type VpcEndpointConnectionNotificationInput interface {
	pulumi.Input

	ToVpcEndpointConnectionNotificationOutput() VpcEndpointConnectionNotificationOutput
	ToVpcEndpointConnectionNotificationOutputWithContext(ctx context.Context) VpcEndpointConnectionNotificationOutput
}

func (*VpcEndpointConnectionNotification) ElementType() reflect.Type {
	return reflect.TypeOf((**VpcEndpointConnectionNotification)(nil)).Elem()
}

func (i *VpcEndpointConnectionNotification) ToVpcEndpointConnectionNotificationOutput() VpcEndpointConnectionNotificationOutput {
	return i.ToVpcEndpointConnectionNotificationOutputWithContext(context.Background())
}

func (i *VpcEndpointConnectionNotification) ToVpcEndpointConnectionNotificationOutputWithContext(ctx context.Context) VpcEndpointConnectionNotificationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpcEndpointConnectionNotificationOutput)
}

func (i *VpcEndpointConnectionNotification) ToOutput(ctx context.Context) pulumix.Output[*VpcEndpointConnectionNotification] {
	return pulumix.Output[*VpcEndpointConnectionNotification]{
		OutputState: i.ToVpcEndpointConnectionNotificationOutputWithContext(ctx).OutputState,
	}
}

type VpcEndpointConnectionNotificationOutput struct{ *pulumi.OutputState }

func (VpcEndpointConnectionNotificationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VpcEndpointConnectionNotification)(nil)).Elem()
}

func (o VpcEndpointConnectionNotificationOutput) ToVpcEndpointConnectionNotificationOutput() VpcEndpointConnectionNotificationOutput {
	return o
}

func (o VpcEndpointConnectionNotificationOutput) ToVpcEndpointConnectionNotificationOutputWithContext(ctx context.Context) VpcEndpointConnectionNotificationOutput {
	return o
}

func (o VpcEndpointConnectionNotificationOutput) ToOutput(ctx context.Context) pulumix.Output[*VpcEndpointConnectionNotification] {
	return pulumix.Output[*VpcEndpointConnectionNotification]{
		OutputState: o.OutputState,
	}
}

func (o VpcEndpointConnectionNotificationOutput) ConnectionEvents() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VpcEndpointConnectionNotification) pulumi.StringArrayOutput { return v.ConnectionEvents }).(pulumi.StringArrayOutput)
}

func (o VpcEndpointConnectionNotificationOutput) ConnectionNotificationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcEndpointConnectionNotification) pulumi.StringOutput { return v.ConnectionNotificationArn }).(pulumi.StringOutput)
}

func (o VpcEndpointConnectionNotificationOutput) ServiceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpcEndpointConnectionNotification) pulumi.StringPtrOutput { return v.ServiceId }).(pulumi.StringPtrOutput)
}

func (o VpcEndpointConnectionNotificationOutput) VpcEndpointId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpcEndpointConnectionNotification) pulumi.StringPtrOutput { return v.VpcEndpointId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VpcEndpointConnectionNotificationInput)(nil)).Elem(), &VpcEndpointConnectionNotification{})
	pulumi.RegisterOutputType(VpcEndpointConnectionNotificationOutput{})
}
