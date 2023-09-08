// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sso

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The assignee's type, user/group
type AssignmentPrincipalType string

const (
	AssignmentPrincipalTypeUser  = AssignmentPrincipalType("USER")
	AssignmentPrincipalTypeGroup = AssignmentPrincipalType("GROUP")
)

func (AssignmentPrincipalType) ElementType() reflect.Type {
	return reflect.TypeOf((*AssignmentPrincipalType)(nil)).Elem()
}

func (e AssignmentPrincipalType) ToAssignmentPrincipalTypeOutput() AssignmentPrincipalTypeOutput {
	return pulumi.ToOutput(e).(AssignmentPrincipalTypeOutput)
}

func (e AssignmentPrincipalType) ToAssignmentPrincipalTypeOutputWithContext(ctx context.Context) AssignmentPrincipalTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(AssignmentPrincipalTypeOutput)
}

func (e AssignmentPrincipalType) ToAssignmentPrincipalTypePtrOutput() AssignmentPrincipalTypePtrOutput {
	return e.ToAssignmentPrincipalTypePtrOutputWithContext(context.Background())
}

func (e AssignmentPrincipalType) ToAssignmentPrincipalTypePtrOutputWithContext(ctx context.Context) AssignmentPrincipalTypePtrOutput {
	return AssignmentPrincipalType(e).ToAssignmentPrincipalTypeOutputWithContext(ctx).ToAssignmentPrincipalTypePtrOutputWithContext(ctx)
}

func (e AssignmentPrincipalType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssignmentPrincipalType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssignmentPrincipalType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e AssignmentPrincipalType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type AssignmentPrincipalTypeOutput struct{ *pulumi.OutputState }

func (AssignmentPrincipalTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssignmentPrincipalType)(nil)).Elem()
}

func (o AssignmentPrincipalTypeOutput) ToAssignmentPrincipalTypeOutput() AssignmentPrincipalTypeOutput {
	return o
}

func (o AssignmentPrincipalTypeOutput) ToAssignmentPrincipalTypeOutputWithContext(ctx context.Context) AssignmentPrincipalTypeOutput {
	return o
}

func (o AssignmentPrincipalTypeOutput) ToAssignmentPrincipalTypePtrOutput() AssignmentPrincipalTypePtrOutput {
	return o.ToAssignmentPrincipalTypePtrOutputWithContext(context.Background())
}

func (o AssignmentPrincipalTypeOutput) ToAssignmentPrincipalTypePtrOutputWithContext(ctx context.Context) AssignmentPrincipalTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AssignmentPrincipalType) *AssignmentPrincipalType {
		return &v
	}).(AssignmentPrincipalTypePtrOutput)
}

func (o AssignmentPrincipalTypeOutput) ToOutput(ctx context.Context) pulumix.Output[AssignmentPrincipalType] {
	return pulumix.Output[AssignmentPrincipalType]{
		OutputState: o.OutputState,
	}
}

func (o AssignmentPrincipalTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AssignmentPrincipalTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssignmentPrincipalType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AssignmentPrincipalTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssignmentPrincipalTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssignmentPrincipalType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AssignmentPrincipalTypePtrOutput struct{ *pulumi.OutputState }

func (AssignmentPrincipalTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AssignmentPrincipalType)(nil)).Elem()
}

func (o AssignmentPrincipalTypePtrOutput) ToAssignmentPrincipalTypePtrOutput() AssignmentPrincipalTypePtrOutput {
	return o
}

func (o AssignmentPrincipalTypePtrOutput) ToAssignmentPrincipalTypePtrOutputWithContext(ctx context.Context) AssignmentPrincipalTypePtrOutput {
	return o
}

func (o AssignmentPrincipalTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*AssignmentPrincipalType] {
	return pulumix.Output[*AssignmentPrincipalType]{
		OutputState: o.OutputState,
	}
}

func (o AssignmentPrincipalTypePtrOutput) Elem() AssignmentPrincipalTypeOutput {
	return o.ApplyT(func(v *AssignmentPrincipalType) AssignmentPrincipalType {
		if v != nil {
			return *v
		}
		var ret AssignmentPrincipalType
		return ret
	}).(AssignmentPrincipalTypeOutput)
}

func (o AssignmentPrincipalTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssignmentPrincipalTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AssignmentPrincipalType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// AssignmentPrincipalTypeInput is an input type that accepts AssignmentPrincipalTypeArgs and AssignmentPrincipalTypeOutput values.
// You can construct a concrete instance of `AssignmentPrincipalTypeInput` via:
//
//	AssignmentPrincipalTypeArgs{...}
type AssignmentPrincipalTypeInput interface {
	pulumi.Input

	ToAssignmentPrincipalTypeOutput() AssignmentPrincipalTypeOutput
	ToAssignmentPrincipalTypeOutputWithContext(context.Context) AssignmentPrincipalTypeOutput
}

var assignmentPrincipalTypePtrType = reflect.TypeOf((**AssignmentPrincipalType)(nil)).Elem()

type AssignmentPrincipalTypePtrInput interface {
	pulumi.Input

	ToAssignmentPrincipalTypePtrOutput() AssignmentPrincipalTypePtrOutput
	ToAssignmentPrincipalTypePtrOutputWithContext(context.Context) AssignmentPrincipalTypePtrOutput
}

type assignmentPrincipalTypePtr string

func AssignmentPrincipalTypePtr(v string) AssignmentPrincipalTypePtrInput {
	return (*assignmentPrincipalTypePtr)(&v)
}

func (*assignmentPrincipalTypePtr) ElementType() reflect.Type {
	return assignmentPrincipalTypePtrType
}

func (in *assignmentPrincipalTypePtr) ToAssignmentPrincipalTypePtrOutput() AssignmentPrincipalTypePtrOutput {
	return pulumi.ToOutput(in).(AssignmentPrincipalTypePtrOutput)
}

func (in *assignmentPrincipalTypePtr) ToAssignmentPrincipalTypePtrOutputWithContext(ctx context.Context) AssignmentPrincipalTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(AssignmentPrincipalTypePtrOutput)
}

func (in *assignmentPrincipalTypePtr) ToOutput(ctx context.Context) pulumix.Output[*AssignmentPrincipalType] {
	return pulumix.Output[*AssignmentPrincipalType]{
		OutputState: in.ToAssignmentPrincipalTypePtrOutputWithContext(ctx).OutputState,
	}
}

// The type of resource to be provsioned to, only aws account now
type AssignmentTargetType string

const (
	AssignmentTargetTypeAwsAccount = AssignmentTargetType("AWS_ACCOUNT")
)

func (AssignmentTargetType) ElementType() reflect.Type {
	return reflect.TypeOf((*AssignmentTargetType)(nil)).Elem()
}

func (e AssignmentTargetType) ToAssignmentTargetTypeOutput() AssignmentTargetTypeOutput {
	return pulumi.ToOutput(e).(AssignmentTargetTypeOutput)
}

func (e AssignmentTargetType) ToAssignmentTargetTypeOutputWithContext(ctx context.Context) AssignmentTargetTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(AssignmentTargetTypeOutput)
}

func (e AssignmentTargetType) ToAssignmentTargetTypePtrOutput() AssignmentTargetTypePtrOutput {
	return e.ToAssignmentTargetTypePtrOutputWithContext(context.Background())
}

func (e AssignmentTargetType) ToAssignmentTargetTypePtrOutputWithContext(ctx context.Context) AssignmentTargetTypePtrOutput {
	return AssignmentTargetType(e).ToAssignmentTargetTypeOutputWithContext(ctx).ToAssignmentTargetTypePtrOutputWithContext(ctx)
}

func (e AssignmentTargetType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssignmentTargetType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssignmentTargetType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e AssignmentTargetType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type AssignmentTargetTypeOutput struct{ *pulumi.OutputState }

func (AssignmentTargetTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssignmentTargetType)(nil)).Elem()
}

func (o AssignmentTargetTypeOutput) ToAssignmentTargetTypeOutput() AssignmentTargetTypeOutput {
	return o
}

func (o AssignmentTargetTypeOutput) ToAssignmentTargetTypeOutputWithContext(ctx context.Context) AssignmentTargetTypeOutput {
	return o
}

func (o AssignmentTargetTypeOutput) ToAssignmentTargetTypePtrOutput() AssignmentTargetTypePtrOutput {
	return o.ToAssignmentTargetTypePtrOutputWithContext(context.Background())
}

func (o AssignmentTargetTypeOutput) ToAssignmentTargetTypePtrOutputWithContext(ctx context.Context) AssignmentTargetTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AssignmentTargetType) *AssignmentTargetType {
		return &v
	}).(AssignmentTargetTypePtrOutput)
}

func (o AssignmentTargetTypeOutput) ToOutput(ctx context.Context) pulumix.Output[AssignmentTargetType] {
	return pulumix.Output[AssignmentTargetType]{
		OutputState: o.OutputState,
	}
}

func (o AssignmentTargetTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AssignmentTargetTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssignmentTargetType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AssignmentTargetTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssignmentTargetTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssignmentTargetType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AssignmentTargetTypePtrOutput struct{ *pulumi.OutputState }

func (AssignmentTargetTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AssignmentTargetType)(nil)).Elem()
}

func (o AssignmentTargetTypePtrOutput) ToAssignmentTargetTypePtrOutput() AssignmentTargetTypePtrOutput {
	return o
}

func (o AssignmentTargetTypePtrOutput) ToAssignmentTargetTypePtrOutputWithContext(ctx context.Context) AssignmentTargetTypePtrOutput {
	return o
}

func (o AssignmentTargetTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*AssignmentTargetType] {
	return pulumix.Output[*AssignmentTargetType]{
		OutputState: o.OutputState,
	}
}

func (o AssignmentTargetTypePtrOutput) Elem() AssignmentTargetTypeOutput {
	return o.ApplyT(func(v *AssignmentTargetType) AssignmentTargetType {
		if v != nil {
			return *v
		}
		var ret AssignmentTargetType
		return ret
	}).(AssignmentTargetTypeOutput)
}

func (o AssignmentTargetTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssignmentTargetTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AssignmentTargetType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// AssignmentTargetTypeInput is an input type that accepts AssignmentTargetTypeArgs and AssignmentTargetTypeOutput values.
// You can construct a concrete instance of `AssignmentTargetTypeInput` via:
//
//	AssignmentTargetTypeArgs{...}
type AssignmentTargetTypeInput interface {
	pulumi.Input

	ToAssignmentTargetTypeOutput() AssignmentTargetTypeOutput
	ToAssignmentTargetTypeOutputWithContext(context.Context) AssignmentTargetTypeOutput
}

var assignmentTargetTypePtrType = reflect.TypeOf((**AssignmentTargetType)(nil)).Elem()

type AssignmentTargetTypePtrInput interface {
	pulumi.Input

	ToAssignmentTargetTypePtrOutput() AssignmentTargetTypePtrOutput
	ToAssignmentTargetTypePtrOutputWithContext(context.Context) AssignmentTargetTypePtrOutput
}

type assignmentTargetTypePtr string

func AssignmentTargetTypePtr(v string) AssignmentTargetTypePtrInput {
	return (*assignmentTargetTypePtr)(&v)
}

func (*assignmentTargetTypePtr) ElementType() reflect.Type {
	return assignmentTargetTypePtrType
}

func (in *assignmentTargetTypePtr) ToAssignmentTargetTypePtrOutput() AssignmentTargetTypePtrOutput {
	return pulumi.ToOutput(in).(AssignmentTargetTypePtrOutput)
}

func (in *assignmentTargetTypePtr) ToAssignmentTargetTypePtrOutputWithContext(ctx context.Context) AssignmentTargetTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(AssignmentTargetTypePtrOutput)
}

func (in *assignmentTargetTypePtr) ToOutput(ctx context.Context) pulumix.Output[*AssignmentTargetType] {
	return pulumix.Output[*AssignmentTargetType]{
		OutputState: in.ToAssignmentTargetTypePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AssignmentPrincipalTypeInput)(nil)).Elem(), AssignmentPrincipalType("USER"))
	pulumi.RegisterInputType(reflect.TypeOf((*AssignmentPrincipalTypePtrInput)(nil)).Elem(), AssignmentPrincipalType("USER"))
	pulumi.RegisterInputType(reflect.TypeOf((*AssignmentTargetTypeInput)(nil)).Elem(), AssignmentTargetType("AWS_ACCOUNT"))
	pulumi.RegisterInputType(reflect.TypeOf((*AssignmentTargetTypePtrInput)(nil)).Elem(), AssignmentTargetType("AWS_ACCOUNT"))
	pulumi.RegisterOutputType(AssignmentPrincipalTypeOutput{})
	pulumi.RegisterOutputType(AssignmentPrincipalTypePtrOutput{})
	pulumi.RegisterOutputType(AssignmentTargetTypeOutput{})
	pulumi.RegisterOutputType(AssignmentTargetTypePtrOutput{})
}
