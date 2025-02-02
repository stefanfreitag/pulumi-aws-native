// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package macie

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

// The regex or s3 object to use for the AllowList.
type AllowListCriteria struct {
}

// AllowListCriteriaInput is an input type that accepts AllowListCriteriaArgs and AllowListCriteriaOutput values.
// You can construct a concrete instance of `AllowListCriteriaInput` via:
//
//	AllowListCriteriaArgs{...}
type AllowListCriteriaInput interface {
	pulumi.Input

	ToAllowListCriteriaOutput() AllowListCriteriaOutput
	ToAllowListCriteriaOutputWithContext(context.Context) AllowListCriteriaOutput
}

// The regex or s3 object to use for the AllowList.
type AllowListCriteriaArgs struct {
}

func (AllowListCriteriaArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AllowListCriteria)(nil)).Elem()
}

func (i AllowListCriteriaArgs) ToAllowListCriteriaOutput() AllowListCriteriaOutput {
	return i.ToAllowListCriteriaOutputWithContext(context.Background())
}

func (i AllowListCriteriaArgs) ToAllowListCriteriaOutputWithContext(ctx context.Context) AllowListCriteriaOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AllowListCriteriaOutput)
}

// The regex or s3 object to use for the AllowList.
type AllowListCriteriaOutput struct{ *pulumi.OutputState }

func (AllowListCriteriaOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AllowListCriteria)(nil)).Elem()
}

func (o AllowListCriteriaOutput) ToAllowListCriteriaOutput() AllowListCriteriaOutput {
	return o
}

func (o AllowListCriteriaOutput) ToAllowListCriteriaOutputWithContext(ctx context.Context) AllowListCriteriaOutput {
	return o
}

type AllowListCriteriaPtrOutput struct{ *pulumi.OutputState }

func (AllowListCriteriaPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AllowListCriteria)(nil)).Elem()
}

func (o AllowListCriteriaPtrOutput) ToAllowListCriteriaPtrOutput() AllowListCriteriaPtrOutput {
	return o
}

func (o AllowListCriteriaPtrOutput) ToAllowListCriteriaPtrOutputWithContext(ctx context.Context) AllowListCriteriaPtrOutput {
	return o
}

func (o AllowListCriteriaPtrOutput) Elem() AllowListCriteriaOutput {
	return o.ApplyT(func(v *AllowListCriteria) AllowListCriteria {
		if v != nil {
			return *v
		}
		var ret AllowListCriteria
		return ret
	}).(AllowListCriteriaOutput)
}

// A key-value pair to associate with a resource.
type AllowListTag struct {
	// The tag's key.
	Key string `pulumi:"key"`
	// The tag's value.
	Value string `pulumi:"value"`
}

// A key-value pair to associate with a resource.
type CustomDataIdentifierTag struct {
	// The tag's key.
	Key string `pulumi:"key"`
	// The tag's value.
	Value string `pulumi:"value"`
}

type FindingsFilterCriterionAdditionalProperties struct {
	Eq  []string `pulumi:"eq"`
	Gt  *int     `pulumi:"gt"`
	Gte *int     `pulumi:"gte"`
	Lt  *int     `pulumi:"lt"`
	Lte *int     `pulumi:"lte"`
	Neq []string `pulumi:"neq"`
}

// FindingsFilterCriterionAdditionalPropertiesInput is an input type that accepts FindingsFilterCriterionAdditionalPropertiesArgs and FindingsFilterCriterionAdditionalPropertiesOutput values.
// You can construct a concrete instance of `FindingsFilterCriterionAdditionalPropertiesInput` via:
//
//	FindingsFilterCriterionAdditionalPropertiesArgs{...}
type FindingsFilterCriterionAdditionalPropertiesInput interface {
	pulumi.Input

	ToFindingsFilterCriterionAdditionalPropertiesOutput() FindingsFilterCriterionAdditionalPropertiesOutput
	ToFindingsFilterCriterionAdditionalPropertiesOutputWithContext(context.Context) FindingsFilterCriterionAdditionalPropertiesOutput
}

type FindingsFilterCriterionAdditionalPropertiesArgs struct {
	Eq  pulumi.StringArrayInput `pulumi:"eq"`
	Gt  pulumi.IntPtrInput      `pulumi:"gt"`
	Gte pulumi.IntPtrInput      `pulumi:"gte"`
	Lt  pulumi.IntPtrInput      `pulumi:"lt"`
	Lte pulumi.IntPtrInput      `pulumi:"lte"`
	Neq pulumi.StringArrayInput `pulumi:"neq"`
}

func (FindingsFilterCriterionAdditionalPropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*FindingsFilterCriterionAdditionalProperties)(nil)).Elem()
}

func (i FindingsFilterCriterionAdditionalPropertiesArgs) ToFindingsFilterCriterionAdditionalPropertiesOutput() FindingsFilterCriterionAdditionalPropertiesOutput {
	return i.ToFindingsFilterCriterionAdditionalPropertiesOutputWithContext(context.Background())
}

func (i FindingsFilterCriterionAdditionalPropertiesArgs) ToFindingsFilterCriterionAdditionalPropertiesOutputWithContext(ctx context.Context) FindingsFilterCriterionAdditionalPropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FindingsFilterCriterionAdditionalPropertiesOutput)
}

// FindingsFilterCriterionAdditionalPropertiesMapInput is an input type that accepts FindingsFilterCriterionAdditionalPropertiesMap and FindingsFilterCriterionAdditionalPropertiesMapOutput values.
// You can construct a concrete instance of `FindingsFilterCriterionAdditionalPropertiesMapInput` via:
//
//	FindingsFilterCriterionAdditionalPropertiesMap{ "key": FindingsFilterCriterionAdditionalPropertiesArgs{...} }
type FindingsFilterCriterionAdditionalPropertiesMapInput interface {
	pulumi.Input

	ToFindingsFilterCriterionAdditionalPropertiesMapOutput() FindingsFilterCriterionAdditionalPropertiesMapOutput
	ToFindingsFilterCriterionAdditionalPropertiesMapOutputWithContext(context.Context) FindingsFilterCriterionAdditionalPropertiesMapOutput
}

type FindingsFilterCriterionAdditionalPropertiesMap map[string]FindingsFilterCriterionAdditionalPropertiesInput

func (FindingsFilterCriterionAdditionalPropertiesMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]FindingsFilterCriterionAdditionalProperties)(nil)).Elem()
}

func (i FindingsFilterCriterionAdditionalPropertiesMap) ToFindingsFilterCriterionAdditionalPropertiesMapOutput() FindingsFilterCriterionAdditionalPropertiesMapOutput {
	return i.ToFindingsFilterCriterionAdditionalPropertiesMapOutputWithContext(context.Background())
}

func (i FindingsFilterCriterionAdditionalPropertiesMap) ToFindingsFilterCriterionAdditionalPropertiesMapOutputWithContext(ctx context.Context) FindingsFilterCriterionAdditionalPropertiesMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FindingsFilterCriterionAdditionalPropertiesMapOutput)
}

type FindingsFilterCriterionAdditionalPropertiesOutput struct{ *pulumi.OutputState }

func (FindingsFilterCriterionAdditionalPropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FindingsFilterCriterionAdditionalProperties)(nil)).Elem()
}

func (o FindingsFilterCriterionAdditionalPropertiesOutput) ToFindingsFilterCriterionAdditionalPropertiesOutput() FindingsFilterCriterionAdditionalPropertiesOutput {
	return o
}

func (o FindingsFilterCriterionAdditionalPropertiesOutput) ToFindingsFilterCriterionAdditionalPropertiesOutputWithContext(ctx context.Context) FindingsFilterCriterionAdditionalPropertiesOutput {
	return o
}

func (o FindingsFilterCriterionAdditionalPropertiesOutput) Eq() pulumi.StringArrayOutput {
	return o.ApplyT(func(v FindingsFilterCriterionAdditionalProperties) []string { return v.Eq }).(pulumi.StringArrayOutput)
}

func (o FindingsFilterCriterionAdditionalPropertiesOutput) Gt() pulumi.IntPtrOutput {
	return o.ApplyT(func(v FindingsFilterCriterionAdditionalProperties) *int { return v.Gt }).(pulumi.IntPtrOutput)
}

func (o FindingsFilterCriterionAdditionalPropertiesOutput) Gte() pulumi.IntPtrOutput {
	return o.ApplyT(func(v FindingsFilterCriterionAdditionalProperties) *int { return v.Gte }).(pulumi.IntPtrOutput)
}

func (o FindingsFilterCriterionAdditionalPropertiesOutput) Lt() pulumi.IntPtrOutput {
	return o.ApplyT(func(v FindingsFilterCriterionAdditionalProperties) *int { return v.Lt }).(pulumi.IntPtrOutput)
}

func (o FindingsFilterCriterionAdditionalPropertiesOutput) Lte() pulumi.IntPtrOutput {
	return o.ApplyT(func(v FindingsFilterCriterionAdditionalProperties) *int { return v.Lte }).(pulumi.IntPtrOutput)
}

func (o FindingsFilterCriterionAdditionalPropertiesOutput) Neq() pulumi.StringArrayOutput {
	return o.ApplyT(func(v FindingsFilterCriterionAdditionalProperties) []string { return v.Neq }).(pulumi.StringArrayOutput)
}

type FindingsFilterCriterionAdditionalPropertiesMapOutput struct{ *pulumi.OutputState }

func (FindingsFilterCriterionAdditionalPropertiesMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]FindingsFilterCriterionAdditionalProperties)(nil)).Elem()
}

func (o FindingsFilterCriterionAdditionalPropertiesMapOutput) ToFindingsFilterCriterionAdditionalPropertiesMapOutput() FindingsFilterCriterionAdditionalPropertiesMapOutput {
	return o
}

func (o FindingsFilterCriterionAdditionalPropertiesMapOutput) ToFindingsFilterCriterionAdditionalPropertiesMapOutputWithContext(ctx context.Context) FindingsFilterCriterionAdditionalPropertiesMapOutput {
	return o
}

func (o FindingsFilterCriterionAdditionalPropertiesMapOutput) MapIndex(k pulumi.StringInput) FindingsFilterCriterionAdditionalPropertiesOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) FindingsFilterCriterionAdditionalProperties {
		return vs[0].(map[string]FindingsFilterCriterionAdditionalProperties)[vs[1].(string)]
	}).(FindingsFilterCriterionAdditionalPropertiesOutput)
}

type FindingsFilterFindingCriteria struct {
	Criterion map[string]FindingsFilterCriterionAdditionalProperties `pulumi:"criterion"`
}

// FindingsFilterFindingCriteriaInput is an input type that accepts FindingsFilterFindingCriteriaArgs and FindingsFilterFindingCriteriaOutput values.
// You can construct a concrete instance of `FindingsFilterFindingCriteriaInput` via:
//
//	FindingsFilterFindingCriteriaArgs{...}
type FindingsFilterFindingCriteriaInput interface {
	pulumi.Input

	ToFindingsFilterFindingCriteriaOutput() FindingsFilterFindingCriteriaOutput
	ToFindingsFilterFindingCriteriaOutputWithContext(context.Context) FindingsFilterFindingCriteriaOutput
}

type FindingsFilterFindingCriteriaArgs struct {
	Criterion FindingsFilterCriterionAdditionalPropertiesMapInput `pulumi:"criterion"`
}

func (FindingsFilterFindingCriteriaArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*FindingsFilterFindingCriteria)(nil)).Elem()
}

func (i FindingsFilterFindingCriteriaArgs) ToFindingsFilterFindingCriteriaOutput() FindingsFilterFindingCriteriaOutput {
	return i.ToFindingsFilterFindingCriteriaOutputWithContext(context.Background())
}

func (i FindingsFilterFindingCriteriaArgs) ToFindingsFilterFindingCriteriaOutputWithContext(ctx context.Context) FindingsFilterFindingCriteriaOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FindingsFilterFindingCriteriaOutput)
}

type FindingsFilterFindingCriteriaOutput struct{ *pulumi.OutputState }

func (FindingsFilterFindingCriteriaOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FindingsFilterFindingCriteria)(nil)).Elem()
}

func (o FindingsFilterFindingCriteriaOutput) ToFindingsFilterFindingCriteriaOutput() FindingsFilterFindingCriteriaOutput {
	return o
}

func (o FindingsFilterFindingCriteriaOutput) ToFindingsFilterFindingCriteriaOutputWithContext(ctx context.Context) FindingsFilterFindingCriteriaOutput {
	return o
}

func (o FindingsFilterFindingCriteriaOutput) Criterion() FindingsFilterCriterionAdditionalPropertiesMapOutput {
	return o.ApplyT(func(v FindingsFilterFindingCriteria) map[string]FindingsFilterCriterionAdditionalProperties {
		return v.Criterion
	}).(FindingsFilterCriterionAdditionalPropertiesMapOutput)
}

type FindingsFilterFindingCriteriaPtrOutput struct{ *pulumi.OutputState }

func (FindingsFilterFindingCriteriaPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FindingsFilterFindingCriteria)(nil)).Elem()
}

func (o FindingsFilterFindingCriteriaPtrOutput) ToFindingsFilterFindingCriteriaPtrOutput() FindingsFilterFindingCriteriaPtrOutput {
	return o
}

func (o FindingsFilterFindingCriteriaPtrOutput) ToFindingsFilterFindingCriteriaPtrOutputWithContext(ctx context.Context) FindingsFilterFindingCriteriaPtrOutput {
	return o
}

func (o FindingsFilterFindingCriteriaPtrOutput) Elem() FindingsFilterFindingCriteriaOutput {
	return o.ApplyT(func(v *FindingsFilterFindingCriteria) FindingsFilterFindingCriteria {
		if v != nil {
			return *v
		}
		var ret FindingsFilterFindingCriteria
		return ret
	}).(FindingsFilterFindingCriteriaOutput)
}

func (o FindingsFilterFindingCriteriaPtrOutput) Criterion() FindingsFilterCriterionAdditionalPropertiesMapOutput {
	return o.ApplyT(func(v *FindingsFilterFindingCriteria) map[string]FindingsFilterCriterionAdditionalProperties {
		if v == nil {
			return nil
		}
		return v.Criterion
	}).(FindingsFilterCriterionAdditionalPropertiesMapOutput)
}

// A key-value pair to associate with a resource.
type FindingsFilterTag struct {
	// The tag's key.
	Key string `pulumi:"key"`
	// The tag's value.
	Value string `pulumi:"value"`
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AllowListCriteriaInput)(nil)).Elem(), AllowListCriteriaArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*FindingsFilterCriterionAdditionalPropertiesInput)(nil)).Elem(), FindingsFilterCriterionAdditionalPropertiesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*FindingsFilterCriterionAdditionalPropertiesMapInput)(nil)).Elem(), FindingsFilterCriterionAdditionalPropertiesMap{})
	pulumi.RegisterInputType(reflect.TypeOf((*FindingsFilterFindingCriteriaInput)(nil)).Elem(), FindingsFilterFindingCriteriaArgs{})
	pulumi.RegisterOutputType(AllowListCriteriaOutput{})
	pulumi.RegisterOutputType(AllowListCriteriaPtrOutput{})
	pulumi.RegisterOutputType(FindingsFilterCriterionAdditionalPropertiesOutput{})
	pulumi.RegisterOutputType(FindingsFilterCriterionAdditionalPropertiesMapOutput{})
	pulumi.RegisterOutputType(FindingsFilterFindingCriteriaOutput{})
	pulumi.RegisterOutputType(FindingsFilterFindingCriteriaPtrOutput{})
}
