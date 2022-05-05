// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appmesh

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppMesh::VirtualService
//
// Deprecated: VirtualService is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type VirtualService struct {
	pulumi.CustomResourceState

	Arn                pulumi.StringOutput          `pulumi:"arn"`
	MeshName           pulumi.StringOutput          `pulumi:"meshName"`
	MeshOwner          pulumi.StringPtrOutput       `pulumi:"meshOwner"`
	ResourceOwner      pulumi.StringOutput          `pulumi:"resourceOwner"`
	Spec               VirtualServiceSpecOutput     `pulumi:"spec"`
	Tags               VirtualServiceTagArrayOutput `pulumi:"tags"`
	Uid                pulumi.StringOutput          `pulumi:"uid"`
	VirtualServiceName pulumi.StringOutput          `pulumi:"virtualServiceName"`
}

// NewVirtualService registers a new resource with the given unique name, arguments, and options.
func NewVirtualService(ctx *pulumi.Context,
	name string, args *VirtualServiceArgs, opts ...pulumi.ResourceOption) (*VirtualService, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MeshName == nil {
		return nil, errors.New("invalid value for required argument 'MeshName'")
	}
	if args.Spec == nil {
		return nil, errors.New("invalid value for required argument 'Spec'")
	}
	var resource VirtualService
	err := ctx.RegisterResource("aws-native:appmesh:VirtualService", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVirtualService gets an existing VirtualService resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVirtualService(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VirtualServiceState, opts ...pulumi.ResourceOption) (*VirtualService, error) {
	var resource VirtualService
	err := ctx.ReadResource("aws-native:appmesh:VirtualService", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VirtualService resources.
type virtualServiceState struct {
}

type VirtualServiceState struct {
}

func (VirtualServiceState) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualServiceState)(nil)).Elem()
}

type virtualServiceArgs struct {
	MeshName           string              `pulumi:"meshName"`
	MeshOwner          *string             `pulumi:"meshOwner"`
	Spec               VirtualServiceSpec  `pulumi:"spec"`
	Tags               []VirtualServiceTag `pulumi:"tags"`
	VirtualServiceName *string             `pulumi:"virtualServiceName"`
}

// The set of arguments for constructing a VirtualService resource.
type VirtualServiceArgs struct {
	MeshName           pulumi.StringInput
	MeshOwner          pulumi.StringPtrInput
	Spec               VirtualServiceSpecInput
	Tags               VirtualServiceTagArrayInput
	VirtualServiceName pulumi.StringPtrInput
}

func (VirtualServiceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualServiceArgs)(nil)).Elem()
}

type VirtualServiceInput interface {
	pulumi.Input

	ToVirtualServiceOutput() VirtualServiceOutput
	ToVirtualServiceOutputWithContext(ctx context.Context) VirtualServiceOutput
}

func (*VirtualService) ElementType() reflect.Type {
	return reflect.TypeOf((**VirtualService)(nil)).Elem()
}

func (i *VirtualService) ToVirtualServiceOutput() VirtualServiceOutput {
	return i.ToVirtualServiceOutputWithContext(context.Background())
}

func (i *VirtualService) ToVirtualServiceOutputWithContext(ctx context.Context) VirtualServiceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VirtualServiceOutput)
}

type VirtualServiceOutput struct{ *pulumi.OutputState }

func (VirtualServiceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VirtualService)(nil)).Elem()
}

func (o VirtualServiceOutput) ToVirtualServiceOutput() VirtualServiceOutput {
	return o
}

func (o VirtualServiceOutput) ToVirtualServiceOutputWithContext(ctx context.Context) VirtualServiceOutput {
	return o
}

func (o VirtualServiceOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *VirtualService) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o VirtualServiceOutput) MeshName() pulumi.StringOutput {
	return o.ApplyT(func(v *VirtualService) pulumi.StringOutput { return v.MeshName }).(pulumi.StringOutput)
}

func (o VirtualServiceOutput) MeshOwner() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VirtualService) pulumi.StringPtrOutput { return v.MeshOwner }).(pulumi.StringPtrOutput)
}

func (o VirtualServiceOutput) ResourceOwner() pulumi.StringOutput {
	return o.ApplyT(func(v *VirtualService) pulumi.StringOutput { return v.ResourceOwner }).(pulumi.StringOutput)
}

func (o VirtualServiceOutput) Spec() VirtualServiceSpecOutput {
	return o.ApplyT(func(v *VirtualService) VirtualServiceSpecOutput { return v.Spec }).(VirtualServiceSpecOutput)
}

func (o VirtualServiceOutput) Tags() VirtualServiceTagArrayOutput {
	return o.ApplyT(func(v *VirtualService) VirtualServiceTagArrayOutput { return v.Tags }).(VirtualServiceTagArrayOutput)
}

func (o VirtualServiceOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v *VirtualService) pulumi.StringOutput { return v.Uid }).(pulumi.StringOutput)
}

func (o VirtualServiceOutput) VirtualServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *VirtualService) pulumi.StringOutput { return v.VirtualServiceName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VirtualServiceInput)(nil)).Elem(), &VirtualService{})
	pulumi.RegisterOutputType(VirtualServiceOutput{})
}
