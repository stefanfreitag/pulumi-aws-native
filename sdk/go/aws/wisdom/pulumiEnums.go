// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wisdom

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type AssistantAssociationAssociationType string

const (
	AssistantAssociationAssociationTypeKnowledgeBase = AssistantAssociationAssociationType("KNOWLEDGE_BASE")
)

func (AssistantAssociationAssociationType) ElementType() reflect.Type {
	return reflect.TypeOf((*AssistantAssociationAssociationType)(nil)).Elem()
}

func (e AssistantAssociationAssociationType) ToAssistantAssociationAssociationTypeOutput() AssistantAssociationAssociationTypeOutput {
	return pulumi.ToOutput(e).(AssistantAssociationAssociationTypeOutput)
}

func (e AssistantAssociationAssociationType) ToAssistantAssociationAssociationTypeOutputWithContext(ctx context.Context) AssistantAssociationAssociationTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(AssistantAssociationAssociationTypeOutput)
}

func (e AssistantAssociationAssociationType) ToAssistantAssociationAssociationTypePtrOutput() AssistantAssociationAssociationTypePtrOutput {
	return e.ToAssistantAssociationAssociationTypePtrOutputWithContext(context.Background())
}

func (e AssistantAssociationAssociationType) ToAssistantAssociationAssociationTypePtrOutputWithContext(ctx context.Context) AssistantAssociationAssociationTypePtrOutput {
	return AssistantAssociationAssociationType(e).ToAssistantAssociationAssociationTypeOutputWithContext(ctx).ToAssistantAssociationAssociationTypePtrOutputWithContext(ctx)
}

func (e AssistantAssociationAssociationType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssistantAssociationAssociationType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssistantAssociationAssociationType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e AssistantAssociationAssociationType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type AssistantAssociationAssociationTypeOutput struct{ *pulumi.OutputState }

func (AssistantAssociationAssociationTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssistantAssociationAssociationType)(nil)).Elem()
}

func (o AssistantAssociationAssociationTypeOutput) ToAssistantAssociationAssociationTypeOutput() AssistantAssociationAssociationTypeOutput {
	return o
}

func (o AssistantAssociationAssociationTypeOutput) ToAssistantAssociationAssociationTypeOutputWithContext(ctx context.Context) AssistantAssociationAssociationTypeOutput {
	return o
}

func (o AssistantAssociationAssociationTypeOutput) ToAssistantAssociationAssociationTypePtrOutput() AssistantAssociationAssociationTypePtrOutput {
	return o.ToAssistantAssociationAssociationTypePtrOutputWithContext(context.Background())
}

func (o AssistantAssociationAssociationTypeOutput) ToAssistantAssociationAssociationTypePtrOutputWithContext(ctx context.Context) AssistantAssociationAssociationTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AssistantAssociationAssociationType) *AssistantAssociationAssociationType {
		return &v
	}).(AssistantAssociationAssociationTypePtrOutput)
}

func (o AssistantAssociationAssociationTypeOutput) ToOutput(ctx context.Context) pulumix.Output[AssistantAssociationAssociationType] {
	return pulumix.Output[AssistantAssociationAssociationType]{
		OutputState: o.OutputState,
	}
}

func (o AssistantAssociationAssociationTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AssistantAssociationAssociationTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssistantAssociationAssociationType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AssistantAssociationAssociationTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssistantAssociationAssociationTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssistantAssociationAssociationType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AssistantAssociationAssociationTypePtrOutput struct{ *pulumi.OutputState }

func (AssistantAssociationAssociationTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AssistantAssociationAssociationType)(nil)).Elem()
}

func (o AssistantAssociationAssociationTypePtrOutput) ToAssistantAssociationAssociationTypePtrOutput() AssistantAssociationAssociationTypePtrOutput {
	return o
}

func (o AssistantAssociationAssociationTypePtrOutput) ToAssistantAssociationAssociationTypePtrOutputWithContext(ctx context.Context) AssistantAssociationAssociationTypePtrOutput {
	return o
}

func (o AssistantAssociationAssociationTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*AssistantAssociationAssociationType] {
	return pulumix.Output[*AssistantAssociationAssociationType]{
		OutputState: o.OutputState,
	}
}

func (o AssistantAssociationAssociationTypePtrOutput) Elem() AssistantAssociationAssociationTypeOutput {
	return o.ApplyT(func(v *AssistantAssociationAssociationType) AssistantAssociationAssociationType {
		if v != nil {
			return *v
		}
		var ret AssistantAssociationAssociationType
		return ret
	}).(AssistantAssociationAssociationTypeOutput)
}

func (o AssistantAssociationAssociationTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssistantAssociationAssociationTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AssistantAssociationAssociationType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// AssistantAssociationAssociationTypeInput is an input type that accepts AssistantAssociationAssociationTypeArgs and AssistantAssociationAssociationTypeOutput values.
// You can construct a concrete instance of `AssistantAssociationAssociationTypeInput` via:
//
//	AssistantAssociationAssociationTypeArgs{...}
type AssistantAssociationAssociationTypeInput interface {
	pulumi.Input

	ToAssistantAssociationAssociationTypeOutput() AssistantAssociationAssociationTypeOutput
	ToAssistantAssociationAssociationTypeOutputWithContext(context.Context) AssistantAssociationAssociationTypeOutput
}

var assistantAssociationAssociationTypePtrType = reflect.TypeOf((**AssistantAssociationAssociationType)(nil)).Elem()

type AssistantAssociationAssociationTypePtrInput interface {
	pulumi.Input

	ToAssistantAssociationAssociationTypePtrOutput() AssistantAssociationAssociationTypePtrOutput
	ToAssistantAssociationAssociationTypePtrOutputWithContext(context.Context) AssistantAssociationAssociationTypePtrOutput
}

type assistantAssociationAssociationTypePtr string

func AssistantAssociationAssociationTypePtr(v string) AssistantAssociationAssociationTypePtrInput {
	return (*assistantAssociationAssociationTypePtr)(&v)
}

func (*assistantAssociationAssociationTypePtr) ElementType() reflect.Type {
	return assistantAssociationAssociationTypePtrType
}

func (in *assistantAssociationAssociationTypePtr) ToAssistantAssociationAssociationTypePtrOutput() AssistantAssociationAssociationTypePtrOutput {
	return pulumi.ToOutput(in).(AssistantAssociationAssociationTypePtrOutput)
}

func (in *assistantAssociationAssociationTypePtr) ToAssistantAssociationAssociationTypePtrOutputWithContext(ctx context.Context) AssistantAssociationAssociationTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(AssistantAssociationAssociationTypePtrOutput)
}

func (in *assistantAssociationAssociationTypePtr) ToOutput(ctx context.Context) pulumix.Output[*AssistantAssociationAssociationType] {
	return pulumix.Output[*AssistantAssociationAssociationType]{
		OutputState: in.ToAssistantAssociationAssociationTypePtrOutputWithContext(ctx).OutputState,
	}
}

type AssistantType string

const (
	AssistantTypeAgent = AssistantType("AGENT")
)

func (AssistantType) ElementType() reflect.Type {
	return reflect.TypeOf((*AssistantType)(nil)).Elem()
}

func (e AssistantType) ToAssistantTypeOutput() AssistantTypeOutput {
	return pulumi.ToOutput(e).(AssistantTypeOutput)
}

func (e AssistantType) ToAssistantTypeOutputWithContext(ctx context.Context) AssistantTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(AssistantTypeOutput)
}

func (e AssistantType) ToAssistantTypePtrOutput() AssistantTypePtrOutput {
	return e.ToAssistantTypePtrOutputWithContext(context.Background())
}

func (e AssistantType) ToAssistantTypePtrOutputWithContext(ctx context.Context) AssistantTypePtrOutput {
	return AssistantType(e).ToAssistantTypeOutputWithContext(ctx).ToAssistantTypePtrOutputWithContext(ctx)
}

func (e AssistantType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssistantType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssistantType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e AssistantType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type AssistantTypeOutput struct{ *pulumi.OutputState }

func (AssistantTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssistantType)(nil)).Elem()
}

func (o AssistantTypeOutput) ToAssistantTypeOutput() AssistantTypeOutput {
	return o
}

func (o AssistantTypeOutput) ToAssistantTypeOutputWithContext(ctx context.Context) AssistantTypeOutput {
	return o
}

func (o AssistantTypeOutput) ToAssistantTypePtrOutput() AssistantTypePtrOutput {
	return o.ToAssistantTypePtrOutputWithContext(context.Background())
}

func (o AssistantTypeOutput) ToAssistantTypePtrOutputWithContext(ctx context.Context) AssistantTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AssistantType) *AssistantType {
		return &v
	}).(AssistantTypePtrOutput)
}

func (o AssistantTypeOutput) ToOutput(ctx context.Context) pulumix.Output[AssistantType] {
	return pulumix.Output[AssistantType]{
		OutputState: o.OutputState,
	}
}

func (o AssistantTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AssistantTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssistantType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AssistantTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssistantTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssistantType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AssistantTypePtrOutput struct{ *pulumi.OutputState }

func (AssistantTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AssistantType)(nil)).Elem()
}

func (o AssistantTypePtrOutput) ToAssistantTypePtrOutput() AssistantTypePtrOutput {
	return o
}

func (o AssistantTypePtrOutput) ToAssistantTypePtrOutputWithContext(ctx context.Context) AssistantTypePtrOutput {
	return o
}

func (o AssistantTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*AssistantType] {
	return pulumix.Output[*AssistantType]{
		OutputState: o.OutputState,
	}
}

func (o AssistantTypePtrOutput) Elem() AssistantTypeOutput {
	return o.ApplyT(func(v *AssistantType) AssistantType {
		if v != nil {
			return *v
		}
		var ret AssistantType
		return ret
	}).(AssistantTypeOutput)
}

func (o AssistantTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssistantTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AssistantType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// AssistantTypeInput is an input type that accepts AssistantTypeArgs and AssistantTypeOutput values.
// You can construct a concrete instance of `AssistantTypeInput` via:
//
//	AssistantTypeArgs{...}
type AssistantTypeInput interface {
	pulumi.Input

	ToAssistantTypeOutput() AssistantTypeOutput
	ToAssistantTypeOutputWithContext(context.Context) AssistantTypeOutput
}

var assistantTypePtrType = reflect.TypeOf((**AssistantType)(nil)).Elem()

type AssistantTypePtrInput interface {
	pulumi.Input

	ToAssistantTypePtrOutput() AssistantTypePtrOutput
	ToAssistantTypePtrOutputWithContext(context.Context) AssistantTypePtrOutput
}

type assistantTypePtr string

func AssistantTypePtr(v string) AssistantTypePtrInput {
	return (*assistantTypePtr)(&v)
}

func (*assistantTypePtr) ElementType() reflect.Type {
	return assistantTypePtrType
}

func (in *assistantTypePtr) ToAssistantTypePtrOutput() AssistantTypePtrOutput {
	return pulumi.ToOutput(in).(AssistantTypePtrOutput)
}

func (in *assistantTypePtr) ToAssistantTypePtrOutputWithContext(ctx context.Context) AssistantTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(AssistantTypePtrOutput)
}

func (in *assistantTypePtr) ToOutput(ctx context.Context) pulumix.Output[*AssistantType] {
	return pulumix.Output[*AssistantType]{
		OutputState: in.ToAssistantTypePtrOutputWithContext(ctx).OutputState,
	}
}

type KnowledgeBaseType string

const (
	KnowledgeBaseTypeExternal = KnowledgeBaseType("EXTERNAL")
	KnowledgeBaseTypeCustom   = KnowledgeBaseType("CUSTOM")
)

func (KnowledgeBaseType) ElementType() reflect.Type {
	return reflect.TypeOf((*KnowledgeBaseType)(nil)).Elem()
}

func (e KnowledgeBaseType) ToKnowledgeBaseTypeOutput() KnowledgeBaseTypeOutput {
	return pulumi.ToOutput(e).(KnowledgeBaseTypeOutput)
}

func (e KnowledgeBaseType) ToKnowledgeBaseTypeOutputWithContext(ctx context.Context) KnowledgeBaseTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(KnowledgeBaseTypeOutput)
}

func (e KnowledgeBaseType) ToKnowledgeBaseTypePtrOutput() KnowledgeBaseTypePtrOutput {
	return e.ToKnowledgeBaseTypePtrOutputWithContext(context.Background())
}

func (e KnowledgeBaseType) ToKnowledgeBaseTypePtrOutputWithContext(ctx context.Context) KnowledgeBaseTypePtrOutput {
	return KnowledgeBaseType(e).ToKnowledgeBaseTypeOutputWithContext(ctx).ToKnowledgeBaseTypePtrOutputWithContext(ctx)
}

func (e KnowledgeBaseType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e KnowledgeBaseType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e KnowledgeBaseType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e KnowledgeBaseType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type KnowledgeBaseTypeOutput struct{ *pulumi.OutputState }

func (KnowledgeBaseTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*KnowledgeBaseType)(nil)).Elem()
}

func (o KnowledgeBaseTypeOutput) ToKnowledgeBaseTypeOutput() KnowledgeBaseTypeOutput {
	return o
}

func (o KnowledgeBaseTypeOutput) ToKnowledgeBaseTypeOutputWithContext(ctx context.Context) KnowledgeBaseTypeOutput {
	return o
}

func (o KnowledgeBaseTypeOutput) ToKnowledgeBaseTypePtrOutput() KnowledgeBaseTypePtrOutput {
	return o.ToKnowledgeBaseTypePtrOutputWithContext(context.Background())
}

func (o KnowledgeBaseTypeOutput) ToKnowledgeBaseTypePtrOutputWithContext(ctx context.Context) KnowledgeBaseTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v KnowledgeBaseType) *KnowledgeBaseType {
		return &v
	}).(KnowledgeBaseTypePtrOutput)
}

func (o KnowledgeBaseTypeOutput) ToOutput(ctx context.Context) pulumix.Output[KnowledgeBaseType] {
	return pulumix.Output[KnowledgeBaseType]{
		OutputState: o.OutputState,
	}
}

func (o KnowledgeBaseTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o KnowledgeBaseTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e KnowledgeBaseType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o KnowledgeBaseTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o KnowledgeBaseTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e KnowledgeBaseType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type KnowledgeBaseTypePtrOutput struct{ *pulumi.OutputState }

func (KnowledgeBaseTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**KnowledgeBaseType)(nil)).Elem()
}

func (o KnowledgeBaseTypePtrOutput) ToKnowledgeBaseTypePtrOutput() KnowledgeBaseTypePtrOutput {
	return o
}

func (o KnowledgeBaseTypePtrOutput) ToKnowledgeBaseTypePtrOutputWithContext(ctx context.Context) KnowledgeBaseTypePtrOutput {
	return o
}

func (o KnowledgeBaseTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*KnowledgeBaseType] {
	return pulumix.Output[*KnowledgeBaseType]{
		OutputState: o.OutputState,
	}
}

func (o KnowledgeBaseTypePtrOutput) Elem() KnowledgeBaseTypeOutput {
	return o.ApplyT(func(v *KnowledgeBaseType) KnowledgeBaseType {
		if v != nil {
			return *v
		}
		var ret KnowledgeBaseType
		return ret
	}).(KnowledgeBaseTypeOutput)
}

func (o KnowledgeBaseTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o KnowledgeBaseTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *KnowledgeBaseType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// KnowledgeBaseTypeInput is an input type that accepts KnowledgeBaseTypeArgs and KnowledgeBaseTypeOutput values.
// You can construct a concrete instance of `KnowledgeBaseTypeInput` via:
//
//	KnowledgeBaseTypeArgs{...}
type KnowledgeBaseTypeInput interface {
	pulumi.Input

	ToKnowledgeBaseTypeOutput() KnowledgeBaseTypeOutput
	ToKnowledgeBaseTypeOutputWithContext(context.Context) KnowledgeBaseTypeOutput
}

var knowledgeBaseTypePtrType = reflect.TypeOf((**KnowledgeBaseType)(nil)).Elem()

type KnowledgeBaseTypePtrInput interface {
	pulumi.Input

	ToKnowledgeBaseTypePtrOutput() KnowledgeBaseTypePtrOutput
	ToKnowledgeBaseTypePtrOutputWithContext(context.Context) KnowledgeBaseTypePtrOutput
}

type knowledgeBaseTypePtr string

func KnowledgeBaseTypePtr(v string) KnowledgeBaseTypePtrInput {
	return (*knowledgeBaseTypePtr)(&v)
}

func (*knowledgeBaseTypePtr) ElementType() reflect.Type {
	return knowledgeBaseTypePtrType
}

func (in *knowledgeBaseTypePtr) ToKnowledgeBaseTypePtrOutput() KnowledgeBaseTypePtrOutput {
	return pulumi.ToOutput(in).(KnowledgeBaseTypePtrOutput)
}

func (in *knowledgeBaseTypePtr) ToKnowledgeBaseTypePtrOutputWithContext(ctx context.Context) KnowledgeBaseTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(KnowledgeBaseTypePtrOutput)
}

func (in *knowledgeBaseTypePtr) ToOutput(ctx context.Context) pulumix.Output[*KnowledgeBaseType] {
	return pulumix.Output[*KnowledgeBaseType]{
		OutputState: in.ToKnowledgeBaseTypePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AssistantAssociationAssociationTypeInput)(nil)).Elem(), AssistantAssociationAssociationType("KNOWLEDGE_BASE"))
	pulumi.RegisterInputType(reflect.TypeOf((*AssistantAssociationAssociationTypePtrInput)(nil)).Elem(), AssistantAssociationAssociationType("KNOWLEDGE_BASE"))
	pulumi.RegisterInputType(reflect.TypeOf((*AssistantTypeInput)(nil)).Elem(), AssistantType("AGENT"))
	pulumi.RegisterInputType(reflect.TypeOf((*AssistantTypePtrInput)(nil)).Elem(), AssistantType("AGENT"))
	pulumi.RegisterInputType(reflect.TypeOf((*KnowledgeBaseTypeInput)(nil)).Elem(), KnowledgeBaseType("EXTERNAL"))
	pulumi.RegisterInputType(reflect.TypeOf((*KnowledgeBaseTypePtrInput)(nil)).Elem(), KnowledgeBaseType("EXTERNAL"))
	pulumi.RegisterOutputType(AssistantAssociationAssociationTypeOutput{})
	pulumi.RegisterOutputType(AssistantAssociationAssociationTypePtrOutput{})
	pulumi.RegisterOutputType(AssistantTypeOutput{})
	pulumi.RegisterOutputType(AssistantTypePtrOutput{})
	pulumi.RegisterOutputType(KnowledgeBaseTypeOutput{})
	pulumi.RegisterOutputType(KnowledgeBaseTypePtrOutput{})
}
