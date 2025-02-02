// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dax

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type ClusterSseSpecification struct {
	SseEnabled *bool `pulumi:"sseEnabled"`
}

// ClusterSseSpecificationInput is an input type that accepts ClusterSseSpecificationArgs and ClusterSseSpecificationOutput values.
// You can construct a concrete instance of `ClusterSseSpecificationInput` via:
//
//	ClusterSseSpecificationArgs{...}
type ClusterSseSpecificationInput interface {
	pulumi.Input

	ToClusterSseSpecificationOutput() ClusterSseSpecificationOutput
	ToClusterSseSpecificationOutputWithContext(context.Context) ClusterSseSpecificationOutput
}

type ClusterSseSpecificationArgs struct {
	SseEnabled pulumi.BoolPtrInput `pulumi:"sseEnabled"`
}

func (ClusterSseSpecificationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterSseSpecification)(nil)).Elem()
}

func (i ClusterSseSpecificationArgs) ToClusterSseSpecificationOutput() ClusterSseSpecificationOutput {
	return i.ToClusterSseSpecificationOutputWithContext(context.Background())
}

func (i ClusterSseSpecificationArgs) ToClusterSseSpecificationOutputWithContext(ctx context.Context) ClusterSseSpecificationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterSseSpecificationOutput)
}

func (i ClusterSseSpecificationArgs) ToClusterSseSpecificationPtrOutput() ClusterSseSpecificationPtrOutput {
	return i.ToClusterSseSpecificationPtrOutputWithContext(context.Background())
}

func (i ClusterSseSpecificationArgs) ToClusterSseSpecificationPtrOutputWithContext(ctx context.Context) ClusterSseSpecificationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterSseSpecificationOutput).ToClusterSseSpecificationPtrOutputWithContext(ctx)
}

// ClusterSseSpecificationPtrInput is an input type that accepts ClusterSseSpecificationArgs, ClusterSseSpecificationPtr and ClusterSseSpecificationPtrOutput values.
// You can construct a concrete instance of `ClusterSseSpecificationPtrInput` via:
//
//	        ClusterSseSpecificationArgs{...}
//
//	or:
//
//	        nil
type ClusterSseSpecificationPtrInput interface {
	pulumi.Input

	ToClusterSseSpecificationPtrOutput() ClusterSseSpecificationPtrOutput
	ToClusterSseSpecificationPtrOutputWithContext(context.Context) ClusterSseSpecificationPtrOutput
}

type clusterSseSpecificationPtrType ClusterSseSpecificationArgs

func ClusterSseSpecificationPtr(v *ClusterSseSpecificationArgs) ClusterSseSpecificationPtrInput {
	return (*clusterSseSpecificationPtrType)(v)
}

func (*clusterSseSpecificationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ClusterSseSpecification)(nil)).Elem()
}

func (i *clusterSseSpecificationPtrType) ToClusterSseSpecificationPtrOutput() ClusterSseSpecificationPtrOutput {
	return i.ToClusterSseSpecificationPtrOutputWithContext(context.Background())
}

func (i *clusterSseSpecificationPtrType) ToClusterSseSpecificationPtrOutputWithContext(ctx context.Context) ClusterSseSpecificationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterSseSpecificationPtrOutput)
}

type ClusterSseSpecificationOutput struct{ *pulumi.OutputState }

func (ClusterSseSpecificationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterSseSpecification)(nil)).Elem()
}

func (o ClusterSseSpecificationOutput) ToClusterSseSpecificationOutput() ClusterSseSpecificationOutput {
	return o
}

func (o ClusterSseSpecificationOutput) ToClusterSseSpecificationOutputWithContext(ctx context.Context) ClusterSseSpecificationOutput {
	return o
}

func (o ClusterSseSpecificationOutput) ToClusterSseSpecificationPtrOutput() ClusterSseSpecificationPtrOutput {
	return o.ToClusterSseSpecificationPtrOutputWithContext(context.Background())
}

func (o ClusterSseSpecificationOutput) ToClusterSseSpecificationPtrOutputWithContext(ctx context.Context) ClusterSseSpecificationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ClusterSseSpecification) *ClusterSseSpecification {
		return &v
	}).(ClusterSseSpecificationPtrOutput)
}

func (o ClusterSseSpecificationOutput) SseEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v ClusterSseSpecification) *bool { return v.SseEnabled }).(pulumi.BoolPtrOutput)
}

type ClusterSseSpecificationPtrOutput struct{ *pulumi.OutputState }

func (ClusterSseSpecificationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ClusterSseSpecification)(nil)).Elem()
}

func (o ClusterSseSpecificationPtrOutput) ToClusterSseSpecificationPtrOutput() ClusterSseSpecificationPtrOutput {
	return o
}

func (o ClusterSseSpecificationPtrOutput) ToClusterSseSpecificationPtrOutputWithContext(ctx context.Context) ClusterSseSpecificationPtrOutput {
	return o
}

func (o ClusterSseSpecificationPtrOutput) Elem() ClusterSseSpecificationOutput {
	return o.ApplyT(func(v *ClusterSseSpecification) ClusterSseSpecification {
		if v != nil {
			return *v
		}
		var ret ClusterSseSpecification
		return ret
	}).(ClusterSseSpecificationOutput)
}

func (o ClusterSseSpecificationPtrOutput) SseEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ClusterSseSpecification) *bool {
		if v == nil {
			return nil
		}
		return v.SseEnabled
	}).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterSseSpecificationInput)(nil)).Elem(), ClusterSseSpecificationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterSseSpecificationPtrInput)(nil)).Elem(), ClusterSseSpecificationArgs{})
	pulumi.RegisterOutputType(ClusterSseSpecificationOutput{})
	pulumi.RegisterOutputType(ClusterSseSpecificationPtrOutput{})
}
