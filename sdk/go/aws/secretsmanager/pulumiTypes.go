// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package secretsmanager

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type RotationScheduleHostedRotationLambda struct {
	KmsKeyArn             *string `pulumi:"kmsKeyArn"`
	MasterSecretArn       *string `pulumi:"masterSecretArn"`
	MasterSecretKmsKeyArn *string `pulumi:"masterSecretKmsKeyArn"`
	RotationLambdaName    *string `pulumi:"rotationLambdaName"`
	RotationType          string  `pulumi:"rotationType"`
	VpcSecurityGroupIds   *string `pulumi:"vpcSecurityGroupIds"`
	VpcSubnetIds          *string `pulumi:"vpcSubnetIds"`
}

// RotationScheduleHostedRotationLambdaInput is an input type that accepts RotationScheduleHostedRotationLambdaArgs and RotationScheduleHostedRotationLambdaOutput values.
// You can construct a concrete instance of `RotationScheduleHostedRotationLambdaInput` via:
//
//          RotationScheduleHostedRotationLambdaArgs{...}
type RotationScheduleHostedRotationLambdaInput interface {
	pulumi.Input

	ToRotationScheduleHostedRotationLambdaOutput() RotationScheduleHostedRotationLambdaOutput
	ToRotationScheduleHostedRotationLambdaOutputWithContext(context.Context) RotationScheduleHostedRotationLambdaOutput
}

type RotationScheduleHostedRotationLambdaArgs struct {
	KmsKeyArn             pulumi.StringPtrInput `pulumi:"kmsKeyArn"`
	MasterSecretArn       pulumi.StringPtrInput `pulumi:"masterSecretArn"`
	MasterSecretKmsKeyArn pulumi.StringPtrInput `pulumi:"masterSecretKmsKeyArn"`
	RotationLambdaName    pulumi.StringPtrInput `pulumi:"rotationLambdaName"`
	RotationType          pulumi.StringInput    `pulumi:"rotationType"`
	VpcSecurityGroupIds   pulumi.StringPtrInput `pulumi:"vpcSecurityGroupIds"`
	VpcSubnetIds          pulumi.StringPtrInput `pulumi:"vpcSubnetIds"`
}

func (RotationScheduleHostedRotationLambdaArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*RotationScheduleHostedRotationLambda)(nil)).Elem()
}

func (i RotationScheduleHostedRotationLambdaArgs) ToRotationScheduleHostedRotationLambdaOutput() RotationScheduleHostedRotationLambdaOutput {
	return i.ToRotationScheduleHostedRotationLambdaOutputWithContext(context.Background())
}

func (i RotationScheduleHostedRotationLambdaArgs) ToRotationScheduleHostedRotationLambdaOutputWithContext(ctx context.Context) RotationScheduleHostedRotationLambdaOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RotationScheduleHostedRotationLambdaOutput)
}

func (i RotationScheduleHostedRotationLambdaArgs) ToRotationScheduleHostedRotationLambdaPtrOutput() RotationScheduleHostedRotationLambdaPtrOutput {
	return i.ToRotationScheduleHostedRotationLambdaPtrOutputWithContext(context.Background())
}

func (i RotationScheduleHostedRotationLambdaArgs) ToRotationScheduleHostedRotationLambdaPtrOutputWithContext(ctx context.Context) RotationScheduleHostedRotationLambdaPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RotationScheduleHostedRotationLambdaOutput).ToRotationScheduleHostedRotationLambdaPtrOutputWithContext(ctx)
}

// RotationScheduleHostedRotationLambdaPtrInput is an input type that accepts RotationScheduleHostedRotationLambdaArgs, RotationScheduleHostedRotationLambdaPtr and RotationScheduleHostedRotationLambdaPtrOutput values.
// You can construct a concrete instance of `RotationScheduleHostedRotationLambdaPtrInput` via:
//
//          RotationScheduleHostedRotationLambdaArgs{...}
//
//  or:
//
//          nil
type RotationScheduleHostedRotationLambdaPtrInput interface {
	pulumi.Input

	ToRotationScheduleHostedRotationLambdaPtrOutput() RotationScheduleHostedRotationLambdaPtrOutput
	ToRotationScheduleHostedRotationLambdaPtrOutputWithContext(context.Context) RotationScheduleHostedRotationLambdaPtrOutput
}

type rotationScheduleHostedRotationLambdaPtrType RotationScheduleHostedRotationLambdaArgs

func RotationScheduleHostedRotationLambdaPtr(v *RotationScheduleHostedRotationLambdaArgs) RotationScheduleHostedRotationLambdaPtrInput {
	return (*rotationScheduleHostedRotationLambdaPtrType)(v)
}

func (*rotationScheduleHostedRotationLambdaPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**RotationScheduleHostedRotationLambda)(nil)).Elem()
}

func (i *rotationScheduleHostedRotationLambdaPtrType) ToRotationScheduleHostedRotationLambdaPtrOutput() RotationScheduleHostedRotationLambdaPtrOutput {
	return i.ToRotationScheduleHostedRotationLambdaPtrOutputWithContext(context.Background())
}

func (i *rotationScheduleHostedRotationLambdaPtrType) ToRotationScheduleHostedRotationLambdaPtrOutputWithContext(ctx context.Context) RotationScheduleHostedRotationLambdaPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RotationScheduleHostedRotationLambdaPtrOutput)
}

type RotationScheduleHostedRotationLambdaOutput struct{ *pulumi.OutputState }

func (RotationScheduleHostedRotationLambdaOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RotationScheduleHostedRotationLambda)(nil)).Elem()
}

func (o RotationScheduleHostedRotationLambdaOutput) ToRotationScheduleHostedRotationLambdaOutput() RotationScheduleHostedRotationLambdaOutput {
	return o
}

func (o RotationScheduleHostedRotationLambdaOutput) ToRotationScheduleHostedRotationLambdaOutputWithContext(ctx context.Context) RotationScheduleHostedRotationLambdaOutput {
	return o
}

func (o RotationScheduleHostedRotationLambdaOutput) ToRotationScheduleHostedRotationLambdaPtrOutput() RotationScheduleHostedRotationLambdaPtrOutput {
	return o.ToRotationScheduleHostedRotationLambdaPtrOutputWithContext(context.Background())
}

func (o RotationScheduleHostedRotationLambdaOutput) ToRotationScheduleHostedRotationLambdaPtrOutputWithContext(ctx context.Context) RotationScheduleHostedRotationLambdaPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v RotationScheduleHostedRotationLambda) *RotationScheduleHostedRotationLambda {
		return &v
	}).(RotationScheduleHostedRotationLambdaPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaOutput) KmsKeyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v RotationScheduleHostedRotationLambda) *string { return v.KmsKeyArn }).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaOutput) MasterSecretArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v RotationScheduleHostedRotationLambda) *string { return v.MasterSecretArn }).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaOutput) MasterSecretKmsKeyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v RotationScheduleHostedRotationLambda) *string { return v.MasterSecretKmsKeyArn }).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaOutput) RotationLambdaName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v RotationScheduleHostedRotationLambda) *string { return v.RotationLambdaName }).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaOutput) RotationType() pulumi.StringOutput {
	return o.ApplyT(func(v RotationScheduleHostedRotationLambda) string { return v.RotationType }).(pulumi.StringOutput)
}

func (o RotationScheduleHostedRotationLambdaOutput) VpcSecurityGroupIds() pulumi.StringPtrOutput {
	return o.ApplyT(func(v RotationScheduleHostedRotationLambda) *string { return v.VpcSecurityGroupIds }).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaOutput) VpcSubnetIds() pulumi.StringPtrOutput {
	return o.ApplyT(func(v RotationScheduleHostedRotationLambda) *string { return v.VpcSubnetIds }).(pulumi.StringPtrOutput)
}

type RotationScheduleHostedRotationLambdaPtrOutput struct{ *pulumi.OutputState }

func (RotationScheduleHostedRotationLambdaPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RotationScheduleHostedRotationLambda)(nil)).Elem()
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) ToRotationScheduleHostedRotationLambdaPtrOutput() RotationScheduleHostedRotationLambdaPtrOutput {
	return o
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) ToRotationScheduleHostedRotationLambdaPtrOutputWithContext(ctx context.Context) RotationScheduleHostedRotationLambdaPtrOutput {
	return o
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) Elem() RotationScheduleHostedRotationLambdaOutput {
	return o.ApplyT(func(v *RotationScheduleHostedRotationLambda) RotationScheduleHostedRotationLambda {
		if v != nil {
			return *v
		}
		var ret RotationScheduleHostedRotationLambda
		return ret
	}).(RotationScheduleHostedRotationLambdaOutput)
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) KmsKeyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RotationScheduleHostedRotationLambda) *string {
		if v == nil {
			return nil
		}
		return v.KmsKeyArn
	}).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) MasterSecretArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RotationScheduleHostedRotationLambda) *string {
		if v == nil {
			return nil
		}
		return v.MasterSecretArn
	}).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) MasterSecretKmsKeyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RotationScheduleHostedRotationLambda) *string {
		if v == nil {
			return nil
		}
		return v.MasterSecretKmsKeyArn
	}).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) RotationLambdaName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RotationScheduleHostedRotationLambda) *string {
		if v == nil {
			return nil
		}
		return v.RotationLambdaName
	}).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) RotationType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RotationScheduleHostedRotationLambda) *string {
		if v == nil {
			return nil
		}
		return &v.RotationType
	}).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) VpcSecurityGroupIds() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RotationScheduleHostedRotationLambda) *string {
		if v == nil {
			return nil
		}
		return v.VpcSecurityGroupIds
	}).(pulumi.StringPtrOutput)
}

func (o RotationScheduleHostedRotationLambdaPtrOutput) VpcSubnetIds() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RotationScheduleHostedRotationLambda) *string {
		if v == nil {
			return nil
		}
		return v.VpcSubnetIds
	}).(pulumi.StringPtrOutput)
}

type RotationScheduleRotationRules struct {
	AutomaticallyAfterDays *int `pulumi:"automaticallyAfterDays"`
}

// RotationScheduleRotationRulesInput is an input type that accepts RotationScheduleRotationRulesArgs and RotationScheduleRotationRulesOutput values.
// You can construct a concrete instance of `RotationScheduleRotationRulesInput` via:
//
//          RotationScheduleRotationRulesArgs{...}
type RotationScheduleRotationRulesInput interface {
	pulumi.Input

	ToRotationScheduleRotationRulesOutput() RotationScheduleRotationRulesOutput
	ToRotationScheduleRotationRulesOutputWithContext(context.Context) RotationScheduleRotationRulesOutput
}

type RotationScheduleRotationRulesArgs struct {
	AutomaticallyAfterDays pulumi.IntPtrInput `pulumi:"automaticallyAfterDays"`
}

func (RotationScheduleRotationRulesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*RotationScheduleRotationRules)(nil)).Elem()
}

func (i RotationScheduleRotationRulesArgs) ToRotationScheduleRotationRulesOutput() RotationScheduleRotationRulesOutput {
	return i.ToRotationScheduleRotationRulesOutputWithContext(context.Background())
}

func (i RotationScheduleRotationRulesArgs) ToRotationScheduleRotationRulesOutputWithContext(ctx context.Context) RotationScheduleRotationRulesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RotationScheduleRotationRulesOutput)
}

func (i RotationScheduleRotationRulesArgs) ToRotationScheduleRotationRulesPtrOutput() RotationScheduleRotationRulesPtrOutput {
	return i.ToRotationScheduleRotationRulesPtrOutputWithContext(context.Background())
}

func (i RotationScheduleRotationRulesArgs) ToRotationScheduleRotationRulesPtrOutputWithContext(ctx context.Context) RotationScheduleRotationRulesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RotationScheduleRotationRulesOutput).ToRotationScheduleRotationRulesPtrOutputWithContext(ctx)
}

// RotationScheduleRotationRulesPtrInput is an input type that accepts RotationScheduleRotationRulesArgs, RotationScheduleRotationRulesPtr and RotationScheduleRotationRulesPtrOutput values.
// You can construct a concrete instance of `RotationScheduleRotationRulesPtrInput` via:
//
//          RotationScheduleRotationRulesArgs{...}
//
//  or:
//
//          nil
type RotationScheduleRotationRulesPtrInput interface {
	pulumi.Input

	ToRotationScheduleRotationRulesPtrOutput() RotationScheduleRotationRulesPtrOutput
	ToRotationScheduleRotationRulesPtrOutputWithContext(context.Context) RotationScheduleRotationRulesPtrOutput
}

type rotationScheduleRotationRulesPtrType RotationScheduleRotationRulesArgs

func RotationScheduleRotationRulesPtr(v *RotationScheduleRotationRulesArgs) RotationScheduleRotationRulesPtrInput {
	return (*rotationScheduleRotationRulesPtrType)(v)
}

func (*rotationScheduleRotationRulesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**RotationScheduleRotationRules)(nil)).Elem()
}

func (i *rotationScheduleRotationRulesPtrType) ToRotationScheduleRotationRulesPtrOutput() RotationScheduleRotationRulesPtrOutput {
	return i.ToRotationScheduleRotationRulesPtrOutputWithContext(context.Background())
}

func (i *rotationScheduleRotationRulesPtrType) ToRotationScheduleRotationRulesPtrOutputWithContext(ctx context.Context) RotationScheduleRotationRulesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RotationScheduleRotationRulesPtrOutput)
}

type RotationScheduleRotationRulesOutput struct{ *pulumi.OutputState }

func (RotationScheduleRotationRulesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RotationScheduleRotationRules)(nil)).Elem()
}

func (o RotationScheduleRotationRulesOutput) ToRotationScheduleRotationRulesOutput() RotationScheduleRotationRulesOutput {
	return o
}

func (o RotationScheduleRotationRulesOutput) ToRotationScheduleRotationRulesOutputWithContext(ctx context.Context) RotationScheduleRotationRulesOutput {
	return o
}

func (o RotationScheduleRotationRulesOutput) ToRotationScheduleRotationRulesPtrOutput() RotationScheduleRotationRulesPtrOutput {
	return o.ToRotationScheduleRotationRulesPtrOutputWithContext(context.Background())
}

func (o RotationScheduleRotationRulesOutput) ToRotationScheduleRotationRulesPtrOutputWithContext(ctx context.Context) RotationScheduleRotationRulesPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v RotationScheduleRotationRules) *RotationScheduleRotationRules {
		return &v
	}).(RotationScheduleRotationRulesPtrOutput)
}

func (o RotationScheduleRotationRulesOutput) AutomaticallyAfterDays() pulumi.IntPtrOutput {
	return o.ApplyT(func(v RotationScheduleRotationRules) *int { return v.AutomaticallyAfterDays }).(pulumi.IntPtrOutput)
}

type RotationScheduleRotationRulesPtrOutput struct{ *pulumi.OutputState }

func (RotationScheduleRotationRulesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RotationScheduleRotationRules)(nil)).Elem()
}

func (o RotationScheduleRotationRulesPtrOutput) ToRotationScheduleRotationRulesPtrOutput() RotationScheduleRotationRulesPtrOutput {
	return o
}

func (o RotationScheduleRotationRulesPtrOutput) ToRotationScheduleRotationRulesPtrOutputWithContext(ctx context.Context) RotationScheduleRotationRulesPtrOutput {
	return o
}

func (o RotationScheduleRotationRulesPtrOutput) Elem() RotationScheduleRotationRulesOutput {
	return o.ApplyT(func(v *RotationScheduleRotationRules) RotationScheduleRotationRules {
		if v != nil {
			return *v
		}
		var ret RotationScheduleRotationRules
		return ret
	}).(RotationScheduleRotationRulesOutput)
}

func (o RotationScheduleRotationRulesPtrOutput) AutomaticallyAfterDays() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *RotationScheduleRotationRules) *int {
		if v == nil {
			return nil
		}
		return v.AutomaticallyAfterDays
	}).(pulumi.IntPtrOutput)
}

type SecretGenerateSecretString struct {
	ExcludeCharacters       *string `pulumi:"excludeCharacters"`
	ExcludeLowercase        *bool   `pulumi:"excludeLowercase"`
	ExcludeNumbers          *bool   `pulumi:"excludeNumbers"`
	ExcludePunctuation      *bool   `pulumi:"excludePunctuation"`
	ExcludeUppercase        *bool   `pulumi:"excludeUppercase"`
	GenerateStringKey       *string `pulumi:"generateStringKey"`
	IncludeSpace            *bool   `pulumi:"includeSpace"`
	PasswordLength          *int    `pulumi:"passwordLength"`
	RequireEachIncludedType *bool   `pulumi:"requireEachIncludedType"`
	SecretStringTemplate    *string `pulumi:"secretStringTemplate"`
}

// SecretGenerateSecretStringInput is an input type that accepts SecretGenerateSecretStringArgs and SecretGenerateSecretStringOutput values.
// You can construct a concrete instance of `SecretGenerateSecretStringInput` via:
//
//          SecretGenerateSecretStringArgs{...}
type SecretGenerateSecretStringInput interface {
	pulumi.Input

	ToSecretGenerateSecretStringOutput() SecretGenerateSecretStringOutput
	ToSecretGenerateSecretStringOutputWithContext(context.Context) SecretGenerateSecretStringOutput
}

type SecretGenerateSecretStringArgs struct {
	ExcludeCharacters       pulumi.StringPtrInput `pulumi:"excludeCharacters"`
	ExcludeLowercase        pulumi.BoolPtrInput   `pulumi:"excludeLowercase"`
	ExcludeNumbers          pulumi.BoolPtrInput   `pulumi:"excludeNumbers"`
	ExcludePunctuation      pulumi.BoolPtrInput   `pulumi:"excludePunctuation"`
	ExcludeUppercase        pulumi.BoolPtrInput   `pulumi:"excludeUppercase"`
	GenerateStringKey       pulumi.StringPtrInput `pulumi:"generateStringKey"`
	IncludeSpace            pulumi.BoolPtrInput   `pulumi:"includeSpace"`
	PasswordLength          pulumi.IntPtrInput    `pulumi:"passwordLength"`
	RequireEachIncludedType pulumi.BoolPtrInput   `pulumi:"requireEachIncludedType"`
	SecretStringTemplate    pulumi.StringPtrInput `pulumi:"secretStringTemplate"`
}

func (SecretGenerateSecretStringArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SecretGenerateSecretString)(nil)).Elem()
}

func (i SecretGenerateSecretStringArgs) ToSecretGenerateSecretStringOutput() SecretGenerateSecretStringOutput {
	return i.ToSecretGenerateSecretStringOutputWithContext(context.Background())
}

func (i SecretGenerateSecretStringArgs) ToSecretGenerateSecretStringOutputWithContext(ctx context.Context) SecretGenerateSecretStringOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretGenerateSecretStringOutput)
}

func (i SecretGenerateSecretStringArgs) ToSecretGenerateSecretStringPtrOutput() SecretGenerateSecretStringPtrOutput {
	return i.ToSecretGenerateSecretStringPtrOutputWithContext(context.Background())
}

func (i SecretGenerateSecretStringArgs) ToSecretGenerateSecretStringPtrOutputWithContext(ctx context.Context) SecretGenerateSecretStringPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretGenerateSecretStringOutput).ToSecretGenerateSecretStringPtrOutputWithContext(ctx)
}

// SecretGenerateSecretStringPtrInput is an input type that accepts SecretGenerateSecretStringArgs, SecretGenerateSecretStringPtr and SecretGenerateSecretStringPtrOutput values.
// You can construct a concrete instance of `SecretGenerateSecretStringPtrInput` via:
//
//          SecretGenerateSecretStringArgs{...}
//
//  or:
//
//          nil
type SecretGenerateSecretStringPtrInput interface {
	pulumi.Input

	ToSecretGenerateSecretStringPtrOutput() SecretGenerateSecretStringPtrOutput
	ToSecretGenerateSecretStringPtrOutputWithContext(context.Context) SecretGenerateSecretStringPtrOutput
}

type secretGenerateSecretStringPtrType SecretGenerateSecretStringArgs

func SecretGenerateSecretStringPtr(v *SecretGenerateSecretStringArgs) SecretGenerateSecretStringPtrInput {
	return (*secretGenerateSecretStringPtrType)(v)
}

func (*secretGenerateSecretStringPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**SecretGenerateSecretString)(nil)).Elem()
}

func (i *secretGenerateSecretStringPtrType) ToSecretGenerateSecretStringPtrOutput() SecretGenerateSecretStringPtrOutput {
	return i.ToSecretGenerateSecretStringPtrOutputWithContext(context.Background())
}

func (i *secretGenerateSecretStringPtrType) ToSecretGenerateSecretStringPtrOutputWithContext(ctx context.Context) SecretGenerateSecretStringPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretGenerateSecretStringPtrOutput)
}

type SecretGenerateSecretStringOutput struct{ *pulumi.OutputState }

func (SecretGenerateSecretStringOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SecretGenerateSecretString)(nil)).Elem()
}

func (o SecretGenerateSecretStringOutput) ToSecretGenerateSecretStringOutput() SecretGenerateSecretStringOutput {
	return o
}

func (o SecretGenerateSecretStringOutput) ToSecretGenerateSecretStringOutputWithContext(ctx context.Context) SecretGenerateSecretStringOutput {
	return o
}

func (o SecretGenerateSecretStringOutput) ToSecretGenerateSecretStringPtrOutput() SecretGenerateSecretStringPtrOutput {
	return o.ToSecretGenerateSecretStringPtrOutputWithContext(context.Background())
}

func (o SecretGenerateSecretStringOutput) ToSecretGenerateSecretStringPtrOutputWithContext(ctx context.Context) SecretGenerateSecretStringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SecretGenerateSecretString) *SecretGenerateSecretString {
		return &v
	}).(SecretGenerateSecretStringPtrOutput)
}

func (o SecretGenerateSecretStringOutput) ExcludeCharacters() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *string { return v.ExcludeCharacters }).(pulumi.StringPtrOutput)
}

func (o SecretGenerateSecretStringOutput) ExcludeLowercase() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *bool { return v.ExcludeLowercase }).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringOutput) ExcludeNumbers() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *bool { return v.ExcludeNumbers }).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringOutput) ExcludePunctuation() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *bool { return v.ExcludePunctuation }).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringOutput) ExcludeUppercase() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *bool { return v.ExcludeUppercase }).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringOutput) GenerateStringKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *string { return v.GenerateStringKey }).(pulumi.StringPtrOutput)
}

func (o SecretGenerateSecretStringOutput) IncludeSpace() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *bool { return v.IncludeSpace }).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringOutput) PasswordLength() pulumi.IntPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *int { return v.PasswordLength }).(pulumi.IntPtrOutput)
}

func (o SecretGenerateSecretStringOutput) RequireEachIncludedType() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *bool { return v.RequireEachIncludedType }).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringOutput) SecretStringTemplate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SecretGenerateSecretString) *string { return v.SecretStringTemplate }).(pulumi.StringPtrOutput)
}

type SecretGenerateSecretStringPtrOutput struct{ *pulumi.OutputState }

func (SecretGenerateSecretStringPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SecretGenerateSecretString)(nil)).Elem()
}

func (o SecretGenerateSecretStringPtrOutput) ToSecretGenerateSecretStringPtrOutput() SecretGenerateSecretStringPtrOutput {
	return o
}

func (o SecretGenerateSecretStringPtrOutput) ToSecretGenerateSecretStringPtrOutputWithContext(ctx context.Context) SecretGenerateSecretStringPtrOutput {
	return o
}

func (o SecretGenerateSecretStringPtrOutput) Elem() SecretGenerateSecretStringOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) SecretGenerateSecretString {
		if v != nil {
			return *v
		}
		var ret SecretGenerateSecretString
		return ret
	}).(SecretGenerateSecretStringOutput)
}

func (o SecretGenerateSecretStringPtrOutput) ExcludeCharacters() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *string {
		if v == nil {
			return nil
		}
		return v.ExcludeCharacters
	}).(pulumi.StringPtrOutput)
}

func (o SecretGenerateSecretStringPtrOutput) ExcludeLowercase() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *bool {
		if v == nil {
			return nil
		}
		return v.ExcludeLowercase
	}).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringPtrOutput) ExcludeNumbers() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *bool {
		if v == nil {
			return nil
		}
		return v.ExcludeNumbers
	}).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringPtrOutput) ExcludePunctuation() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *bool {
		if v == nil {
			return nil
		}
		return v.ExcludePunctuation
	}).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringPtrOutput) ExcludeUppercase() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *bool {
		if v == nil {
			return nil
		}
		return v.ExcludeUppercase
	}).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringPtrOutput) GenerateStringKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *string {
		if v == nil {
			return nil
		}
		return v.GenerateStringKey
	}).(pulumi.StringPtrOutput)
}

func (o SecretGenerateSecretStringPtrOutput) IncludeSpace() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *bool {
		if v == nil {
			return nil
		}
		return v.IncludeSpace
	}).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringPtrOutput) PasswordLength() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *int {
		if v == nil {
			return nil
		}
		return v.PasswordLength
	}).(pulumi.IntPtrOutput)
}

func (o SecretGenerateSecretStringPtrOutput) RequireEachIncludedType() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *bool {
		if v == nil {
			return nil
		}
		return v.RequireEachIncludedType
	}).(pulumi.BoolPtrOutput)
}

func (o SecretGenerateSecretStringPtrOutput) SecretStringTemplate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecretGenerateSecretString) *string {
		if v == nil {
			return nil
		}
		return v.SecretStringTemplate
	}).(pulumi.StringPtrOutput)
}

type SecretReplicaRegion struct {
	KmsKeyId *string `pulumi:"kmsKeyId"`
	Region   string  `pulumi:"region"`
}

// SecretReplicaRegionInput is an input type that accepts SecretReplicaRegionArgs and SecretReplicaRegionOutput values.
// You can construct a concrete instance of `SecretReplicaRegionInput` via:
//
//          SecretReplicaRegionArgs{...}
type SecretReplicaRegionInput interface {
	pulumi.Input

	ToSecretReplicaRegionOutput() SecretReplicaRegionOutput
	ToSecretReplicaRegionOutputWithContext(context.Context) SecretReplicaRegionOutput
}

type SecretReplicaRegionArgs struct {
	KmsKeyId pulumi.StringPtrInput `pulumi:"kmsKeyId"`
	Region   pulumi.StringInput    `pulumi:"region"`
}

func (SecretReplicaRegionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SecretReplicaRegion)(nil)).Elem()
}

func (i SecretReplicaRegionArgs) ToSecretReplicaRegionOutput() SecretReplicaRegionOutput {
	return i.ToSecretReplicaRegionOutputWithContext(context.Background())
}

func (i SecretReplicaRegionArgs) ToSecretReplicaRegionOutputWithContext(ctx context.Context) SecretReplicaRegionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretReplicaRegionOutput)
}

// SecretReplicaRegionArrayInput is an input type that accepts SecretReplicaRegionArray and SecretReplicaRegionArrayOutput values.
// You can construct a concrete instance of `SecretReplicaRegionArrayInput` via:
//
//          SecretReplicaRegionArray{ SecretReplicaRegionArgs{...} }
type SecretReplicaRegionArrayInput interface {
	pulumi.Input

	ToSecretReplicaRegionArrayOutput() SecretReplicaRegionArrayOutput
	ToSecretReplicaRegionArrayOutputWithContext(context.Context) SecretReplicaRegionArrayOutput
}

type SecretReplicaRegionArray []SecretReplicaRegionInput

func (SecretReplicaRegionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]SecretReplicaRegion)(nil)).Elem()
}

func (i SecretReplicaRegionArray) ToSecretReplicaRegionArrayOutput() SecretReplicaRegionArrayOutput {
	return i.ToSecretReplicaRegionArrayOutputWithContext(context.Background())
}

func (i SecretReplicaRegionArray) ToSecretReplicaRegionArrayOutputWithContext(ctx context.Context) SecretReplicaRegionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretReplicaRegionArrayOutput)
}

type SecretReplicaRegionOutput struct{ *pulumi.OutputState }

func (SecretReplicaRegionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SecretReplicaRegion)(nil)).Elem()
}

func (o SecretReplicaRegionOutput) ToSecretReplicaRegionOutput() SecretReplicaRegionOutput {
	return o
}

func (o SecretReplicaRegionOutput) ToSecretReplicaRegionOutputWithContext(ctx context.Context) SecretReplicaRegionOutput {
	return o
}

func (o SecretReplicaRegionOutput) KmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SecretReplicaRegion) *string { return v.KmsKeyId }).(pulumi.StringPtrOutput)
}

func (o SecretReplicaRegionOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v SecretReplicaRegion) string { return v.Region }).(pulumi.StringOutput)
}

type SecretReplicaRegionArrayOutput struct{ *pulumi.OutputState }

func (SecretReplicaRegionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]SecretReplicaRegion)(nil)).Elem()
}

func (o SecretReplicaRegionArrayOutput) ToSecretReplicaRegionArrayOutput() SecretReplicaRegionArrayOutput {
	return o
}

func (o SecretReplicaRegionArrayOutput) ToSecretReplicaRegionArrayOutputWithContext(ctx context.Context) SecretReplicaRegionArrayOutput {
	return o
}

func (o SecretReplicaRegionArrayOutput) Index(i pulumi.IntInput) SecretReplicaRegionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) SecretReplicaRegion {
		return vs[0].([]SecretReplicaRegion)[vs[1].(int)]
	}).(SecretReplicaRegionOutput)
}

type SecretTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// SecretTagInput is an input type that accepts SecretTagArgs and SecretTagOutput values.
// You can construct a concrete instance of `SecretTagInput` via:
//
//          SecretTagArgs{...}
type SecretTagInput interface {
	pulumi.Input

	ToSecretTagOutput() SecretTagOutput
	ToSecretTagOutputWithContext(context.Context) SecretTagOutput
}

type SecretTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (SecretTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SecretTag)(nil)).Elem()
}

func (i SecretTagArgs) ToSecretTagOutput() SecretTagOutput {
	return i.ToSecretTagOutputWithContext(context.Background())
}

func (i SecretTagArgs) ToSecretTagOutputWithContext(ctx context.Context) SecretTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretTagOutput)
}

// SecretTagArrayInput is an input type that accepts SecretTagArray and SecretTagArrayOutput values.
// You can construct a concrete instance of `SecretTagArrayInput` via:
//
//          SecretTagArray{ SecretTagArgs{...} }
type SecretTagArrayInput interface {
	pulumi.Input

	ToSecretTagArrayOutput() SecretTagArrayOutput
	ToSecretTagArrayOutputWithContext(context.Context) SecretTagArrayOutput
}

type SecretTagArray []SecretTagInput

func (SecretTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]SecretTag)(nil)).Elem()
}

func (i SecretTagArray) ToSecretTagArrayOutput() SecretTagArrayOutput {
	return i.ToSecretTagArrayOutputWithContext(context.Background())
}

func (i SecretTagArray) ToSecretTagArrayOutputWithContext(ctx context.Context) SecretTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretTagArrayOutput)
}

type SecretTagOutput struct{ *pulumi.OutputState }

func (SecretTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SecretTag)(nil)).Elem()
}

func (o SecretTagOutput) ToSecretTagOutput() SecretTagOutput {
	return o
}

func (o SecretTagOutput) ToSecretTagOutputWithContext(ctx context.Context) SecretTagOutput {
	return o
}

func (o SecretTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v SecretTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o SecretTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v SecretTag) string { return v.Value }).(pulumi.StringOutput)
}

type SecretTagArrayOutput struct{ *pulumi.OutputState }

func (SecretTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]SecretTag)(nil)).Elem()
}

func (o SecretTagArrayOutput) ToSecretTagArrayOutput() SecretTagArrayOutput {
	return o
}

func (o SecretTagArrayOutput) ToSecretTagArrayOutputWithContext(ctx context.Context) SecretTagArrayOutput {
	return o
}

func (o SecretTagArrayOutput) Index(i pulumi.IntInput) SecretTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) SecretTag {
		return vs[0].([]SecretTag)[vs[1].(int)]
	}).(SecretTagOutput)
}

func init() {
	pulumi.RegisterOutputType(RotationScheduleHostedRotationLambdaOutput{})
	pulumi.RegisterOutputType(RotationScheduleHostedRotationLambdaPtrOutput{})
	pulumi.RegisterOutputType(RotationScheduleRotationRulesOutput{})
	pulumi.RegisterOutputType(RotationScheduleRotationRulesPtrOutput{})
	pulumi.RegisterOutputType(SecretGenerateSecretStringOutput{})
	pulumi.RegisterOutputType(SecretGenerateSecretStringPtrOutput{})
	pulumi.RegisterOutputType(SecretReplicaRegionOutput{})
	pulumi.RegisterOutputType(SecretReplicaRegionArrayOutput{})
	pulumi.RegisterOutputType(SecretTagOutput{})
	pulumi.RegisterOutputType(SecretTagArrayOutput{})
}
