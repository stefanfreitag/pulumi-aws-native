// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalogappregistry

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The type of the CFN Resource for now it's enum CFN_STACK.
type ResourceAssociationResourceType string

const (
	ResourceAssociationResourceTypeCfnStack = ResourceAssociationResourceType("CFN_STACK")
)

func (ResourceAssociationResourceType) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourceAssociationResourceType)(nil)).Elem()
}

func (e ResourceAssociationResourceType) ToResourceAssociationResourceTypeOutput() ResourceAssociationResourceTypeOutput {
	return pulumi.ToOutput(e).(ResourceAssociationResourceTypeOutput)
}

func (e ResourceAssociationResourceType) ToResourceAssociationResourceTypeOutputWithContext(ctx context.Context) ResourceAssociationResourceTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ResourceAssociationResourceTypeOutput)
}

func (e ResourceAssociationResourceType) ToResourceAssociationResourceTypePtrOutput() ResourceAssociationResourceTypePtrOutput {
	return e.ToResourceAssociationResourceTypePtrOutputWithContext(context.Background())
}

func (e ResourceAssociationResourceType) ToResourceAssociationResourceTypePtrOutputWithContext(ctx context.Context) ResourceAssociationResourceTypePtrOutput {
	return ResourceAssociationResourceType(e).ToResourceAssociationResourceTypeOutputWithContext(ctx).ToResourceAssociationResourceTypePtrOutputWithContext(ctx)
}

func (e ResourceAssociationResourceType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ResourceAssociationResourceType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ResourceAssociationResourceType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ResourceAssociationResourceType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ResourceAssociationResourceTypeOutput struct{ *pulumi.OutputState }

func (ResourceAssociationResourceTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourceAssociationResourceType)(nil)).Elem()
}

func (o ResourceAssociationResourceTypeOutput) ToResourceAssociationResourceTypeOutput() ResourceAssociationResourceTypeOutput {
	return o
}

func (o ResourceAssociationResourceTypeOutput) ToResourceAssociationResourceTypeOutputWithContext(ctx context.Context) ResourceAssociationResourceTypeOutput {
	return o
}

func (o ResourceAssociationResourceTypeOutput) ToResourceAssociationResourceTypePtrOutput() ResourceAssociationResourceTypePtrOutput {
	return o.ToResourceAssociationResourceTypePtrOutputWithContext(context.Background())
}

func (o ResourceAssociationResourceTypeOutput) ToResourceAssociationResourceTypePtrOutputWithContext(ctx context.Context) ResourceAssociationResourceTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ResourceAssociationResourceType) *ResourceAssociationResourceType {
		return &v
	}).(ResourceAssociationResourceTypePtrOutput)
}

func (o ResourceAssociationResourceTypeOutput) ToOutput(ctx context.Context) pulumix.Output[ResourceAssociationResourceType] {
	return pulumix.Output[ResourceAssociationResourceType]{
		OutputState: o.OutputState,
	}
}

func (o ResourceAssociationResourceTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ResourceAssociationResourceTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ResourceAssociationResourceType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ResourceAssociationResourceTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ResourceAssociationResourceTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ResourceAssociationResourceType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ResourceAssociationResourceTypePtrOutput struct{ *pulumi.OutputState }

func (ResourceAssociationResourceTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ResourceAssociationResourceType)(nil)).Elem()
}

func (o ResourceAssociationResourceTypePtrOutput) ToResourceAssociationResourceTypePtrOutput() ResourceAssociationResourceTypePtrOutput {
	return o
}

func (o ResourceAssociationResourceTypePtrOutput) ToResourceAssociationResourceTypePtrOutputWithContext(ctx context.Context) ResourceAssociationResourceTypePtrOutput {
	return o
}

func (o ResourceAssociationResourceTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ResourceAssociationResourceType] {
	return pulumix.Output[*ResourceAssociationResourceType]{
		OutputState: o.OutputState,
	}
}

func (o ResourceAssociationResourceTypePtrOutput) Elem() ResourceAssociationResourceTypeOutput {
	return o.ApplyT(func(v *ResourceAssociationResourceType) ResourceAssociationResourceType {
		if v != nil {
			return *v
		}
		var ret ResourceAssociationResourceType
		return ret
	}).(ResourceAssociationResourceTypeOutput)
}

func (o ResourceAssociationResourceTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ResourceAssociationResourceTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ResourceAssociationResourceType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ResourceAssociationResourceTypeInput is an input type that accepts ResourceAssociationResourceTypeArgs and ResourceAssociationResourceTypeOutput values.
// You can construct a concrete instance of `ResourceAssociationResourceTypeInput` via:
//
//	ResourceAssociationResourceTypeArgs{...}
type ResourceAssociationResourceTypeInput interface {
	pulumi.Input

	ToResourceAssociationResourceTypeOutput() ResourceAssociationResourceTypeOutput
	ToResourceAssociationResourceTypeOutputWithContext(context.Context) ResourceAssociationResourceTypeOutput
}

var resourceAssociationResourceTypePtrType = reflect.TypeOf((**ResourceAssociationResourceType)(nil)).Elem()

type ResourceAssociationResourceTypePtrInput interface {
	pulumi.Input

	ToResourceAssociationResourceTypePtrOutput() ResourceAssociationResourceTypePtrOutput
	ToResourceAssociationResourceTypePtrOutputWithContext(context.Context) ResourceAssociationResourceTypePtrOutput
}

type resourceAssociationResourceTypePtr string

func ResourceAssociationResourceTypePtr(v string) ResourceAssociationResourceTypePtrInput {
	return (*resourceAssociationResourceTypePtr)(&v)
}

func (*resourceAssociationResourceTypePtr) ElementType() reflect.Type {
	return resourceAssociationResourceTypePtrType
}

func (in *resourceAssociationResourceTypePtr) ToResourceAssociationResourceTypePtrOutput() ResourceAssociationResourceTypePtrOutput {
	return pulumi.ToOutput(in).(ResourceAssociationResourceTypePtrOutput)
}

func (in *resourceAssociationResourceTypePtr) ToResourceAssociationResourceTypePtrOutputWithContext(ctx context.Context) ResourceAssociationResourceTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ResourceAssociationResourceTypePtrOutput)
}

func (in *resourceAssociationResourceTypePtr) ToOutput(ctx context.Context) pulumix.Output[*ResourceAssociationResourceType] {
	return pulumix.Output[*ResourceAssociationResourceType]{
		OutputState: in.ToResourceAssociationResourceTypePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ResourceAssociationResourceTypeInput)(nil)).Elem(), ResourceAssociationResourceType("CFN_STACK"))
	pulumi.RegisterInputType(reflect.TypeOf((*ResourceAssociationResourceTypePtrInput)(nil)).Elem(), ResourceAssociationResourceType("CFN_STACK"))
	pulumi.RegisterOutputType(ResourceAssociationResourceTypeOutput{})
	pulumi.RegisterOutputType(ResourceAssociationResourceTypePtrOutput{})
}
