// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalog

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type CloudFormationProvisionedProductAcceptLanguage string

const (
	CloudFormationProvisionedProductAcceptLanguageEn = CloudFormationProvisionedProductAcceptLanguage("en")
	CloudFormationProvisionedProductAcceptLanguageJp = CloudFormationProvisionedProductAcceptLanguage("jp")
	CloudFormationProvisionedProductAcceptLanguageZh = CloudFormationProvisionedProductAcceptLanguage("zh")
)

func (CloudFormationProvisionedProductAcceptLanguage) ElementType() reflect.Type {
	return reflect.TypeOf((*CloudFormationProvisionedProductAcceptLanguage)(nil)).Elem()
}

func (e CloudFormationProvisionedProductAcceptLanguage) ToCloudFormationProvisionedProductAcceptLanguageOutput() CloudFormationProvisionedProductAcceptLanguageOutput {
	return pulumi.ToOutput(e).(CloudFormationProvisionedProductAcceptLanguageOutput)
}

func (e CloudFormationProvisionedProductAcceptLanguage) ToCloudFormationProvisionedProductAcceptLanguageOutputWithContext(ctx context.Context) CloudFormationProvisionedProductAcceptLanguageOutput {
	return pulumi.ToOutputWithContext(ctx, e).(CloudFormationProvisionedProductAcceptLanguageOutput)
}

func (e CloudFormationProvisionedProductAcceptLanguage) ToCloudFormationProvisionedProductAcceptLanguagePtrOutput() CloudFormationProvisionedProductAcceptLanguagePtrOutput {
	return e.ToCloudFormationProvisionedProductAcceptLanguagePtrOutputWithContext(context.Background())
}

func (e CloudFormationProvisionedProductAcceptLanguage) ToCloudFormationProvisionedProductAcceptLanguagePtrOutputWithContext(ctx context.Context) CloudFormationProvisionedProductAcceptLanguagePtrOutput {
	return CloudFormationProvisionedProductAcceptLanguage(e).ToCloudFormationProvisionedProductAcceptLanguageOutputWithContext(ctx).ToCloudFormationProvisionedProductAcceptLanguagePtrOutputWithContext(ctx)
}

func (e CloudFormationProvisionedProductAcceptLanguage) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e CloudFormationProvisionedProductAcceptLanguage) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e CloudFormationProvisionedProductAcceptLanguage) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e CloudFormationProvisionedProductAcceptLanguage) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type CloudFormationProvisionedProductAcceptLanguageOutput struct{ *pulumi.OutputState }

func (CloudFormationProvisionedProductAcceptLanguageOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CloudFormationProvisionedProductAcceptLanguage)(nil)).Elem()
}

func (o CloudFormationProvisionedProductAcceptLanguageOutput) ToCloudFormationProvisionedProductAcceptLanguageOutput() CloudFormationProvisionedProductAcceptLanguageOutput {
	return o
}

func (o CloudFormationProvisionedProductAcceptLanguageOutput) ToCloudFormationProvisionedProductAcceptLanguageOutputWithContext(ctx context.Context) CloudFormationProvisionedProductAcceptLanguageOutput {
	return o
}

func (o CloudFormationProvisionedProductAcceptLanguageOutput) ToCloudFormationProvisionedProductAcceptLanguagePtrOutput() CloudFormationProvisionedProductAcceptLanguagePtrOutput {
	return o.ToCloudFormationProvisionedProductAcceptLanguagePtrOutputWithContext(context.Background())
}

func (o CloudFormationProvisionedProductAcceptLanguageOutput) ToCloudFormationProvisionedProductAcceptLanguagePtrOutputWithContext(ctx context.Context) CloudFormationProvisionedProductAcceptLanguagePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v CloudFormationProvisionedProductAcceptLanguage) *CloudFormationProvisionedProductAcceptLanguage {
		return &v
	}).(CloudFormationProvisionedProductAcceptLanguagePtrOutput)
}

func (o CloudFormationProvisionedProductAcceptLanguageOutput) ToOutput(ctx context.Context) pulumix.Output[CloudFormationProvisionedProductAcceptLanguage] {
	return pulumix.Output[CloudFormationProvisionedProductAcceptLanguage]{
		OutputState: o.OutputState,
	}
}

func (o CloudFormationProvisionedProductAcceptLanguageOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o CloudFormationProvisionedProductAcceptLanguageOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e CloudFormationProvisionedProductAcceptLanguage) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o CloudFormationProvisionedProductAcceptLanguageOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o CloudFormationProvisionedProductAcceptLanguageOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e CloudFormationProvisionedProductAcceptLanguage) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type CloudFormationProvisionedProductAcceptLanguagePtrOutput struct{ *pulumi.OutputState }

func (CloudFormationProvisionedProductAcceptLanguagePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CloudFormationProvisionedProductAcceptLanguage)(nil)).Elem()
}

func (o CloudFormationProvisionedProductAcceptLanguagePtrOutput) ToCloudFormationProvisionedProductAcceptLanguagePtrOutput() CloudFormationProvisionedProductAcceptLanguagePtrOutput {
	return o
}

func (o CloudFormationProvisionedProductAcceptLanguagePtrOutput) ToCloudFormationProvisionedProductAcceptLanguagePtrOutputWithContext(ctx context.Context) CloudFormationProvisionedProductAcceptLanguagePtrOutput {
	return o
}

func (o CloudFormationProvisionedProductAcceptLanguagePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*CloudFormationProvisionedProductAcceptLanguage] {
	return pulumix.Output[*CloudFormationProvisionedProductAcceptLanguage]{
		OutputState: o.OutputState,
	}
}

func (o CloudFormationProvisionedProductAcceptLanguagePtrOutput) Elem() CloudFormationProvisionedProductAcceptLanguageOutput {
	return o.ApplyT(func(v *CloudFormationProvisionedProductAcceptLanguage) CloudFormationProvisionedProductAcceptLanguage {
		if v != nil {
			return *v
		}
		var ret CloudFormationProvisionedProductAcceptLanguage
		return ret
	}).(CloudFormationProvisionedProductAcceptLanguageOutput)
}

func (o CloudFormationProvisionedProductAcceptLanguagePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o CloudFormationProvisionedProductAcceptLanguagePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *CloudFormationProvisionedProductAcceptLanguage) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// CloudFormationProvisionedProductAcceptLanguageInput is an input type that accepts CloudFormationProvisionedProductAcceptLanguageArgs and CloudFormationProvisionedProductAcceptLanguageOutput values.
// You can construct a concrete instance of `CloudFormationProvisionedProductAcceptLanguageInput` via:
//
//	CloudFormationProvisionedProductAcceptLanguageArgs{...}
type CloudFormationProvisionedProductAcceptLanguageInput interface {
	pulumi.Input

	ToCloudFormationProvisionedProductAcceptLanguageOutput() CloudFormationProvisionedProductAcceptLanguageOutput
	ToCloudFormationProvisionedProductAcceptLanguageOutputWithContext(context.Context) CloudFormationProvisionedProductAcceptLanguageOutput
}

var cloudFormationProvisionedProductAcceptLanguagePtrType = reflect.TypeOf((**CloudFormationProvisionedProductAcceptLanguage)(nil)).Elem()

type CloudFormationProvisionedProductAcceptLanguagePtrInput interface {
	pulumi.Input

	ToCloudFormationProvisionedProductAcceptLanguagePtrOutput() CloudFormationProvisionedProductAcceptLanguagePtrOutput
	ToCloudFormationProvisionedProductAcceptLanguagePtrOutputWithContext(context.Context) CloudFormationProvisionedProductAcceptLanguagePtrOutput
}

type cloudFormationProvisionedProductAcceptLanguagePtr string

func CloudFormationProvisionedProductAcceptLanguagePtr(v string) CloudFormationProvisionedProductAcceptLanguagePtrInput {
	return (*cloudFormationProvisionedProductAcceptLanguagePtr)(&v)
}

func (*cloudFormationProvisionedProductAcceptLanguagePtr) ElementType() reflect.Type {
	return cloudFormationProvisionedProductAcceptLanguagePtrType
}

func (in *cloudFormationProvisionedProductAcceptLanguagePtr) ToCloudFormationProvisionedProductAcceptLanguagePtrOutput() CloudFormationProvisionedProductAcceptLanguagePtrOutput {
	return pulumi.ToOutput(in).(CloudFormationProvisionedProductAcceptLanguagePtrOutput)
}

func (in *cloudFormationProvisionedProductAcceptLanguagePtr) ToCloudFormationProvisionedProductAcceptLanguagePtrOutputWithContext(ctx context.Context) CloudFormationProvisionedProductAcceptLanguagePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(CloudFormationProvisionedProductAcceptLanguagePtrOutput)
}

func (in *cloudFormationProvisionedProductAcceptLanguagePtr) ToOutput(ctx context.Context) pulumix.Output[*CloudFormationProvisionedProductAcceptLanguage] {
	return pulumix.Output[*CloudFormationProvisionedProductAcceptLanguage]{
		OutputState: in.ToCloudFormationProvisionedProductAcceptLanguagePtrOutputWithContext(ctx).OutputState,
	}
}

type CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType string

const (
	CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeCreate = CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType("CREATE")
	CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeUpdate = CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType("UPDATE")
	CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeDelete = CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType("DELETE")
)

func (CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) ElementType() reflect.Type {
	return reflect.TypeOf((*CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType)(nil)).Elem()
}

func (e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput() CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput {
	return pulumi.ToOutput(e).(CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput)
}

func (e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutputWithContext(ctx context.Context) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput)
}

func (e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput() CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput {
	return e.ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutputWithContext(context.Background())
}

func (e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutputWithContext(ctx context.Context) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput {
	return CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType(e).ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutputWithContext(ctx).ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutputWithContext(ctx)
}

func (e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput struct{ *pulumi.OutputState }

func (CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType)(nil)).Elem()
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput() CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput {
	return o
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutputWithContext(ctx context.Context) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput {
	return o
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput() CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput {
	return o.ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutputWithContext(context.Background())
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutputWithContext(ctx context.Context) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) *CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType {
		return &v
	}).(CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput)
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ToOutput(ctx context.Context) pulumix.Output[CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType] {
	return pulumix.Output[CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType]{
		OutputState: o.OutputState,
	}
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput struct{ *pulumi.OutputState }

func (CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType)(nil)).Elem()
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput() CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput {
	return o
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutputWithContext(ctx context.Context) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput {
	return o
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType] {
	return pulumix.Output[*CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType]{
		OutputState: o.OutputState,
	}
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput) Elem() CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput {
	return o.ApplyT(func(v *CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType {
		if v != nil {
			return *v
		}
		var ret CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType
		return ret
	}).(CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput)
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeInput is an input type that accepts CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeArgs and CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput values.
// You can construct a concrete instance of `CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeInput` via:
//
//	CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeArgs{...}
type CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeInput interface {
	pulumi.Input

	ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput() CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput
	ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutputWithContext(context.Context) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput
}

var cloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrType = reflect.TypeOf((**CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType)(nil)).Elem()

type CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrInput interface {
	pulumi.Input

	ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput() CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput
	ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutputWithContext(context.Context) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput
}

type cloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtr string

func CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtr(v string) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrInput {
	return (*cloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtr)(&v)
}

func (*cloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtr) ElementType() reflect.Type {
	return cloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrType
}

func (in *cloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtr) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput() CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput {
	return pulumi.ToOutput(in).(CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput)
}

func (in *cloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtr) ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutputWithContext(ctx context.Context) CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput)
}

func (in *cloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtr) ToOutput(ctx context.Context) pulumix.Output[*CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType] {
	return pulumix.Output[*CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType]{
		OutputState: in.ToCloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutputWithContext(ctx).OutputState,
	}
}

type ServiceActionAcceptLanguage string

const (
	ServiceActionAcceptLanguageEn = ServiceActionAcceptLanguage("en")
	ServiceActionAcceptLanguageJp = ServiceActionAcceptLanguage("jp")
	ServiceActionAcceptLanguageZh = ServiceActionAcceptLanguage("zh")
)

func (ServiceActionAcceptLanguage) ElementType() reflect.Type {
	return reflect.TypeOf((*ServiceActionAcceptLanguage)(nil)).Elem()
}

func (e ServiceActionAcceptLanguage) ToServiceActionAcceptLanguageOutput() ServiceActionAcceptLanguageOutput {
	return pulumi.ToOutput(e).(ServiceActionAcceptLanguageOutput)
}

func (e ServiceActionAcceptLanguage) ToServiceActionAcceptLanguageOutputWithContext(ctx context.Context) ServiceActionAcceptLanguageOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ServiceActionAcceptLanguageOutput)
}

func (e ServiceActionAcceptLanguage) ToServiceActionAcceptLanguagePtrOutput() ServiceActionAcceptLanguagePtrOutput {
	return e.ToServiceActionAcceptLanguagePtrOutputWithContext(context.Background())
}

func (e ServiceActionAcceptLanguage) ToServiceActionAcceptLanguagePtrOutputWithContext(ctx context.Context) ServiceActionAcceptLanguagePtrOutput {
	return ServiceActionAcceptLanguage(e).ToServiceActionAcceptLanguageOutputWithContext(ctx).ToServiceActionAcceptLanguagePtrOutputWithContext(ctx)
}

func (e ServiceActionAcceptLanguage) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ServiceActionAcceptLanguage) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ServiceActionAcceptLanguage) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ServiceActionAcceptLanguage) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ServiceActionAcceptLanguageOutput struct{ *pulumi.OutputState }

func (ServiceActionAcceptLanguageOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ServiceActionAcceptLanguage)(nil)).Elem()
}

func (o ServiceActionAcceptLanguageOutput) ToServiceActionAcceptLanguageOutput() ServiceActionAcceptLanguageOutput {
	return o
}

func (o ServiceActionAcceptLanguageOutput) ToServiceActionAcceptLanguageOutputWithContext(ctx context.Context) ServiceActionAcceptLanguageOutput {
	return o
}

func (o ServiceActionAcceptLanguageOutput) ToServiceActionAcceptLanguagePtrOutput() ServiceActionAcceptLanguagePtrOutput {
	return o.ToServiceActionAcceptLanguagePtrOutputWithContext(context.Background())
}

func (o ServiceActionAcceptLanguageOutput) ToServiceActionAcceptLanguagePtrOutputWithContext(ctx context.Context) ServiceActionAcceptLanguagePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ServiceActionAcceptLanguage) *ServiceActionAcceptLanguage {
		return &v
	}).(ServiceActionAcceptLanguagePtrOutput)
}

func (o ServiceActionAcceptLanguageOutput) ToOutput(ctx context.Context) pulumix.Output[ServiceActionAcceptLanguage] {
	return pulumix.Output[ServiceActionAcceptLanguage]{
		OutputState: o.OutputState,
	}
}

func (o ServiceActionAcceptLanguageOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ServiceActionAcceptLanguageOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ServiceActionAcceptLanguage) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ServiceActionAcceptLanguageOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ServiceActionAcceptLanguageOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ServiceActionAcceptLanguage) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ServiceActionAcceptLanguagePtrOutput struct{ *pulumi.OutputState }

func (ServiceActionAcceptLanguagePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceActionAcceptLanguage)(nil)).Elem()
}

func (o ServiceActionAcceptLanguagePtrOutput) ToServiceActionAcceptLanguagePtrOutput() ServiceActionAcceptLanguagePtrOutput {
	return o
}

func (o ServiceActionAcceptLanguagePtrOutput) ToServiceActionAcceptLanguagePtrOutputWithContext(ctx context.Context) ServiceActionAcceptLanguagePtrOutput {
	return o
}

func (o ServiceActionAcceptLanguagePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ServiceActionAcceptLanguage] {
	return pulumix.Output[*ServiceActionAcceptLanguage]{
		OutputState: o.OutputState,
	}
}

func (o ServiceActionAcceptLanguagePtrOutput) Elem() ServiceActionAcceptLanguageOutput {
	return o.ApplyT(func(v *ServiceActionAcceptLanguage) ServiceActionAcceptLanguage {
		if v != nil {
			return *v
		}
		var ret ServiceActionAcceptLanguage
		return ret
	}).(ServiceActionAcceptLanguageOutput)
}

func (o ServiceActionAcceptLanguagePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ServiceActionAcceptLanguagePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ServiceActionAcceptLanguage) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ServiceActionAcceptLanguageInput is an input type that accepts ServiceActionAcceptLanguageArgs and ServiceActionAcceptLanguageOutput values.
// You can construct a concrete instance of `ServiceActionAcceptLanguageInput` via:
//
//	ServiceActionAcceptLanguageArgs{...}
type ServiceActionAcceptLanguageInput interface {
	pulumi.Input

	ToServiceActionAcceptLanguageOutput() ServiceActionAcceptLanguageOutput
	ToServiceActionAcceptLanguageOutputWithContext(context.Context) ServiceActionAcceptLanguageOutput
}

var serviceActionAcceptLanguagePtrType = reflect.TypeOf((**ServiceActionAcceptLanguage)(nil)).Elem()

type ServiceActionAcceptLanguagePtrInput interface {
	pulumi.Input

	ToServiceActionAcceptLanguagePtrOutput() ServiceActionAcceptLanguagePtrOutput
	ToServiceActionAcceptLanguagePtrOutputWithContext(context.Context) ServiceActionAcceptLanguagePtrOutput
}

type serviceActionAcceptLanguagePtr string

func ServiceActionAcceptLanguagePtr(v string) ServiceActionAcceptLanguagePtrInput {
	return (*serviceActionAcceptLanguagePtr)(&v)
}

func (*serviceActionAcceptLanguagePtr) ElementType() reflect.Type {
	return serviceActionAcceptLanguagePtrType
}

func (in *serviceActionAcceptLanguagePtr) ToServiceActionAcceptLanguagePtrOutput() ServiceActionAcceptLanguagePtrOutput {
	return pulumi.ToOutput(in).(ServiceActionAcceptLanguagePtrOutput)
}

func (in *serviceActionAcceptLanguagePtr) ToServiceActionAcceptLanguagePtrOutputWithContext(ctx context.Context) ServiceActionAcceptLanguagePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ServiceActionAcceptLanguagePtrOutput)
}

func (in *serviceActionAcceptLanguagePtr) ToOutput(ctx context.Context) pulumix.Output[*ServiceActionAcceptLanguage] {
	return pulumix.Output[*ServiceActionAcceptLanguage]{
		OutputState: in.ToServiceActionAcceptLanguagePtrOutputWithContext(ctx).OutputState,
	}
}

type ServiceActionDefinitionType string

const (
	ServiceActionDefinitionTypeSsmAutomation = ServiceActionDefinitionType("SSM_AUTOMATION")
)

func (ServiceActionDefinitionType) ElementType() reflect.Type {
	return reflect.TypeOf((*ServiceActionDefinitionType)(nil)).Elem()
}

func (e ServiceActionDefinitionType) ToServiceActionDefinitionTypeOutput() ServiceActionDefinitionTypeOutput {
	return pulumi.ToOutput(e).(ServiceActionDefinitionTypeOutput)
}

func (e ServiceActionDefinitionType) ToServiceActionDefinitionTypeOutputWithContext(ctx context.Context) ServiceActionDefinitionTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ServiceActionDefinitionTypeOutput)
}

func (e ServiceActionDefinitionType) ToServiceActionDefinitionTypePtrOutput() ServiceActionDefinitionTypePtrOutput {
	return e.ToServiceActionDefinitionTypePtrOutputWithContext(context.Background())
}

func (e ServiceActionDefinitionType) ToServiceActionDefinitionTypePtrOutputWithContext(ctx context.Context) ServiceActionDefinitionTypePtrOutput {
	return ServiceActionDefinitionType(e).ToServiceActionDefinitionTypeOutputWithContext(ctx).ToServiceActionDefinitionTypePtrOutputWithContext(ctx)
}

func (e ServiceActionDefinitionType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ServiceActionDefinitionType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ServiceActionDefinitionType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ServiceActionDefinitionType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ServiceActionDefinitionTypeOutput struct{ *pulumi.OutputState }

func (ServiceActionDefinitionTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ServiceActionDefinitionType)(nil)).Elem()
}

func (o ServiceActionDefinitionTypeOutput) ToServiceActionDefinitionTypeOutput() ServiceActionDefinitionTypeOutput {
	return o
}

func (o ServiceActionDefinitionTypeOutput) ToServiceActionDefinitionTypeOutputWithContext(ctx context.Context) ServiceActionDefinitionTypeOutput {
	return o
}

func (o ServiceActionDefinitionTypeOutput) ToServiceActionDefinitionTypePtrOutput() ServiceActionDefinitionTypePtrOutput {
	return o.ToServiceActionDefinitionTypePtrOutputWithContext(context.Background())
}

func (o ServiceActionDefinitionTypeOutput) ToServiceActionDefinitionTypePtrOutputWithContext(ctx context.Context) ServiceActionDefinitionTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ServiceActionDefinitionType) *ServiceActionDefinitionType {
		return &v
	}).(ServiceActionDefinitionTypePtrOutput)
}

func (o ServiceActionDefinitionTypeOutput) ToOutput(ctx context.Context) pulumix.Output[ServiceActionDefinitionType] {
	return pulumix.Output[ServiceActionDefinitionType]{
		OutputState: o.OutputState,
	}
}

func (o ServiceActionDefinitionTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ServiceActionDefinitionTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ServiceActionDefinitionType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ServiceActionDefinitionTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ServiceActionDefinitionTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ServiceActionDefinitionType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ServiceActionDefinitionTypePtrOutput struct{ *pulumi.OutputState }

func (ServiceActionDefinitionTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceActionDefinitionType)(nil)).Elem()
}

func (o ServiceActionDefinitionTypePtrOutput) ToServiceActionDefinitionTypePtrOutput() ServiceActionDefinitionTypePtrOutput {
	return o
}

func (o ServiceActionDefinitionTypePtrOutput) ToServiceActionDefinitionTypePtrOutputWithContext(ctx context.Context) ServiceActionDefinitionTypePtrOutput {
	return o
}

func (o ServiceActionDefinitionTypePtrOutput) ToOutput(ctx context.Context) pulumix.Output[*ServiceActionDefinitionType] {
	return pulumix.Output[*ServiceActionDefinitionType]{
		OutputState: o.OutputState,
	}
}

func (o ServiceActionDefinitionTypePtrOutput) Elem() ServiceActionDefinitionTypeOutput {
	return o.ApplyT(func(v *ServiceActionDefinitionType) ServiceActionDefinitionType {
		if v != nil {
			return *v
		}
		var ret ServiceActionDefinitionType
		return ret
	}).(ServiceActionDefinitionTypeOutput)
}

func (o ServiceActionDefinitionTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ServiceActionDefinitionTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ServiceActionDefinitionType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ServiceActionDefinitionTypeInput is an input type that accepts ServiceActionDefinitionTypeArgs and ServiceActionDefinitionTypeOutput values.
// You can construct a concrete instance of `ServiceActionDefinitionTypeInput` via:
//
//	ServiceActionDefinitionTypeArgs{...}
type ServiceActionDefinitionTypeInput interface {
	pulumi.Input

	ToServiceActionDefinitionTypeOutput() ServiceActionDefinitionTypeOutput
	ToServiceActionDefinitionTypeOutputWithContext(context.Context) ServiceActionDefinitionTypeOutput
}

var serviceActionDefinitionTypePtrType = reflect.TypeOf((**ServiceActionDefinitionType)(nil)).Elem()

type ServiceActionDefinitionTypePtrInput interface {
	pulumi.Input

	ToServiceActionDefinitionTypePtrOutput() ServiceActionDefinitionTypePtrOutput
	ToServiceActionDefinitionTypePtrOutputWithContext(context.Context) ServiceActionDefinitionTypePtrOutput
}

type serviceActionDefinitionTypePtr string

func ServiceActionDefinitionTypePtr(v string) ServiceActionDefinitionTypePtrInput {
	return (*serviceActionDefinitionTypePtr)(&v)
}

func (*serviceActionDefinitionTypePtr) ElementType() reflect.Type {
	return serviceActionDefinitionTypePtrType
}

func (in *serviceActionDefinitionTypePtr) ToServiceActionDefinitionTypePtrOutput() ServiceActionDefinitionTypePtrOutput {
	return pulumi.ToOutput(in).(ServiceActionDefinitionTypePtrOutput)
}

func (in *serviceActionDefinitionTypePtr) ToServiceActionDefinitionTypePtrOutputWithContext(ctx context.Context) ServiceActionDefinitionTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ServiceActionDefinitionTypePtrOutput)
}

func (in *serviceActionDefinitionTypePtr) ToOutput(ctx context.Context) pulumix.Output[*ServiceActionDefinitionType] {
	return pulumix.Output[*ServiceActionDefinitionType]{
		OutputState: in.ToServiceActionDefinitionTypePtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CloudFormationProvisionedProductAcceptLanguageInput)(nil)).Elem(), CloudFormationProvisionedProductAcceptLanguage("en"))
	pulumi.RegisterInputType(reflect.TypeOf((*CloudFormationProvisionedProductAcceptLanguagePtrInput)(nil)).Elem(), CloudFormationProvisionedProductAcceptLanguage("en"))
	pulumi.RegisterInputType(reflect.TypeOf((*CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeInput)(nil)).Elem(), CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType("CREATE"))
	pulumi.RegisterInputType(reflect.TypeOf((*CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrInput)(nil)).Elem(), CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationType("CREATE"))
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceActionAcceptLanguageInput)(nil)).Elem(), ServiceActionAcceptLanguage("en"))
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceActionAcceptLanguagePtrInput)(nil)).Elem(), ServiceActionAcceptLanguage("en"))
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceActionDefinitionTypeInput)(nil)).Elem(), ServiceActionDefinitionType("SSM_AUTOMATION"))
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceActionDefinitionTypePtrInput)(nil)).Elem(), ServiceActionDefinitionType("SSM_AUTOMATION"))
	pulumi.RegisterOutputType(CloudFormationProvisionedProductAcceptLanguageOutput{})
	pulumi.RegisterOutputType(CloudFormationProvisionedProductAcceptLanguagePtrOutput{})
	pulumi.RegisterOutputType(CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypeOutput{})
	pulumi.RegisterOutputType(CloudFormationProvisionedProductProvisioningPreferencesStackSetOperationTypePtrOutput{})
	pulumi.RegisterOutputType(ServiceActionAcceptLanguageOutput{})
	pulumi.RegisterOutputType(ServiceActionAcceptLanguagePtrOutput{})
	pulumi.RegisterOutputType(ServiceActionDefinitionTypeOutput{})
	pulumi.RegisterOutputType(ServiceActionDefinitionTypePtrOutput{})
}
