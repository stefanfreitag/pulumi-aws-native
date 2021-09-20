// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package route53resolver

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A key-value pair to associate with a resource.
type FirewallDomainListTag struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key string `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value string `pulumi:"value"`
}

// FirewallDomainListTagInput is an input type that accepts FirewallDomainListTagArgs and FirewallDomainListTagOutput values.
// You can construct a concrete instance of `FirewallDomainListTagInput` via:
//
//          FirewallDomainListTagArgs{...}
type FirewallDomainListTagInput interface {
	pulumi.Input

	ToFirewallDomainListTagOutput() FirewallDomainListTagOutput
	ToFirewallDomainListTagOutputWithContext(context.Context) FirewallDomainListTagOutput
}

// A key-value pair to associate with a resource.
type FirewallDomainListTagArgs struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key pulumi.StringInput `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value pulumi.StringInput `pulumi:"value"`
}

func (FirewallDomainListTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallDomainListTag)(nil)).Elem()
}

func (i FirewallDomainListTagArgs) ToFirewallDomainListTagOutput() FirewallDomainListTagOutput {
	return i.ToFirewallDomainListTagOutputWithContext(context.Background())
}

func (i FirewallDomainListTagArgs) ToFirewallDomainListTagOutputWithContext(ctx context.Context) FirewallDomainListTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallDomainListTagOutput)
}

// FirewallDomainListTagArrayInput is an input type that accepts FirewallDomainListTagArray and FirewallDomainListTagArrayOutput values.
// You can construct a concrete instance of `FirewallDomainListTagArrayInput` via:
//
//          FirewallDomainListTagArray{ FirewallDomainListTagArgs{...} }
type FirewallDomainListTagArrayInput interface {
	pulumi.Input

	ToFirewallDomainListTagArrayOutput() FirewallDomainListTagArrayOutput
	ToFirewallDomainListTagArrayOutputWithContext(context.Context) FirewallDomainListTagArrayOutput
}

type FirewallDomainListTagArray []FirewallDomainListTagInput

func (FirewallDomainListTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]FirewallDomainListTag)(nil)).Elem()
}

func (i FirewallDomainListTagArray) ToFirewallDomainListTagArrayOutput() FirewallDomainListTagArrayOutput {
	return i.ToFirewallDomainListTagArrayOutputWithContext(context.Background())
}

func (i FirewallDomainListTagArray) ToFirewallDomainListTagArrayOutputWithContext(ctx context.Context) FirewallDomainListTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallDomainListTagArrayOutput)
}

// A key-value pair to associate with a resource.
type FirewallDomainListTagOutput struct{ *pulumi.OutputState }

func (FirewallDomainListTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallDomainListTag)(nil)).Elem()
}

func (o FirewallDomainListTagOutput) ToFirewallDomainListTagOutput() FirewallDomainListTagOutput {
	return o
}

func (o FirewallDomainListTagOutput) ToFirewallDomainListTagOutputWithContext(ctx context.Context) FirewallDomainListTagOutput {
	return o
}

// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o FirewallDomainListTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v FirewallDomainListTag) string { return v.Key }).(pulumi.StringOutput)
}

// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o FirewallDomainListTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v FirewallDomainListTag) string { return v.Value }).(pulumi.StringOutput)
}

type FirewallDomainListTagArrayOutput struct{ *pulumi.OutputState }

func (FirewallDomainListTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]FirewallDomainListTag)(nil)).Elem()
}

func (o FirewallDomainListTagArrayOutput) ToFirewallDomainListTagArrayOutput() FirewallDomainListTagArrayOutput {
	return o
}

func (o FirewallDomainListTagArrayOutput) ToFirewallDomainListTagArrayOutputWithContext(ctx context.Context) FirewallDomainListTagArrayOutput {
	return o
}

func (o FirewallDomainListTagArrayOutput) Index(i pulumi.IntInput) FirewallDomainListTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) FirewallDomainListTag {
		return vs[0].([]FirewallDomainListTag)[vs[1].(int)]
	}).(FirewallDomainListTagOutput)
}

// A key-value pair to associate with a resource.
type FirewallRuleGroupAssociationTag struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key string `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value string `pulumi:"value"`
}

// FirewallRuleGroupAssociationTagInput is an input type that accepts FirewallRuleGroupAssociationTagArgs and FirewallRuleGroupAssociationTagOutput values.
// You can construct a concrete instance of `FirewallRuleGroupAssociationTagInput` via:
//
//          FirewallRuleGroupAssociationTagArgs{...}
type FirewallRuleGroupAssociationTagInput interface {
	pulumi.Input

	ToFirewallRuleGroupAssociationTagOutput() FirewallRuleGroupAssociationTagOutput
	ToFirewallRuleGroupAssociationTagOutputWithContext(context.Context) FirewallRuleGroupAssociationTagOutput
}

// A key-value pair to associate with a resource.
type FirewallRuleGroupAssociationTagArgs struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key pulumi.StringInput `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value pulumi.StringInput `pulumi:"value"`
}

func (FirewallRuleGroupAssociationTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallRuleGroupAssociationTag)(nil)).Elem()
}

func (i FirewallRuleGroupAssociationTagArgs) ToFirewallRuleGroupAssociationTagOutput() FirewallRuleGroupAssociationTagOutput {
	return i.ToFirewallRuleGroupAssociationTagOutputWithContext(context.Background())
}

func (i FirewallRuleGroupAssociationTagArgs) ToFirewallRuleGroupAssociationTagOutputWithContext(ctx context.Context) FirewallRuleGroupAssociationTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleGroupAssociationTagOutput)
}

// FirewallRuleGroupAssociationTagArrayInput is an input type that accepts FirewallRuleGroupAssociationTagArray and FirewallRuleGroupAssociationTagArrayOutput values.
// You can construct a concrete instance of `FirewallRuleGroupAssociationTagArrayInput` via:
//
//          FirewallRuleGroupAssociationTagArray{ FirewallRuleGroupAssociationTagArgs{...} }
type FirewallRuleGroupAssociationTagArrayInput interface {
	pulumi.Input

	ToFirewallRuleGroupAssociationTagArrayOutput() FirewallRuleGroupAssociationTagArrayOutput
	ToFirewallRuleGroupAssociationTagArrayOutputWithContext(context.Context) FirewallRuleGroupAssociationTagArrayOutput
}

type FirewallRuleGroupAssociationTagArray []FirewallRuleGroupAssociationTagInput

func (FirewallRuleGroupAssociationTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]FirewallRuleGroupAssociationTag)(nil)).Elem()
}

func (i FirewallRuleGroupAssociationTagArray) ToFirewallRuleGroupAssociationTagArrayOutput() FirewallRuleGroupAssociationTagArrayOutput {
	return i.ToFirewallRuleGroupAssociationTagArrayOutputWithContext(context.Background())
}

func (i FirewallRuleGroupAssociationTagArray) ToFirewallRuleGroupAssociationTagArrayOutputWithContext(ctx context.Context) FirewallRuleGroupAssociationTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleGroupAssociationTagArrayOutput)
}

// A key-value pair to associate with a resource.
type FirewallRuleGroupAssociationTagOutput struct{ *pulumi.OutputState }

func (FirewallRuleGroupAssociationTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallRuleGroupAssociationTag)(nil)).Elem()
}

func (o FirewallRuleGroupAssociationTagOutput) ToFirewallRuleGroupAssociationTagOutput() FirewallRuleGroupAssociationTagOutput {
	return o
}

func (o FirewallRuleGroupAssociationTagOutput) ToFirewallRuleGroupAssociationTagOutputWithContext(ctx context.Context) FirewallRuleGroupAssociationTagOutput {
	return o
}

// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o FirewallRuleGroupAssociationTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v FirewallRuleGroupAssociationTag) string { return v.Key }).(pulumi.StringOutput)
}

// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o FirewallRuleGroupAssociationTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v FirewallRuleGroupAssociationTag) string { return v.Value }).(pulumi.StringOutput)
}

type FirewallRuleGroupAssociationTagArrayOutput struct{ *pulumi.OutputState }

func (FirewallRuleGroupAssociationTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]FirewallRuleGroupAssociationTag)(nil)).Elem()
}

func (o FirewallRuleGroupAssociationTagArrayOutput) ToFirewallRuleGroupAssociationTagArrayOutput() FirewallRuleGroupAssociationTagArrayOutput {
	return o
}

func (o FirewallRuleGroupAssociationTagArrayOutput) ToFirewallRuleGroupAssociationTagArrayOutputWithContext(ctx context.Context) FirewallRuleGroupAssociationTagArrayOutput {
	return o
}

func (o FirewallRuleGroupAssociationTagArrayOutput) Index(i pulumi.IntInput) FirewallRuleGroupAssociationTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) FirewallRuleGroupAssociationTag {
		return vs[0].([]FirewallRuleGroupAssociationTag)[vs[1].(int)]
	}).(FirewallRuleGroupAssociationTagOutput)
}

// Firewall Rule associating the Rule Group to a Domain List
type FirewallRuleGroupFirewallRule struct {
	// Rule Action
	Action FirewallRuleGroupFirewallRuleAction `pulumi:"action"`
	// BlockOverrideDnsType
	BlockOverrideDnsType *FirewallRuleGroupFirewallRuleBlockOverrideDnsType `pulumi:"blockOverrideDnsType"`
	// BlockOverrideDomain
	BlockOverrideDomain *string `pulumi:"blockOverrideDomain"`
	// BlockOverrideTtl
	BlockOverrideTtl *int `pulumi:"blockOverrideTtl"`
	// BlockResponse
	BlockResponse *FirewallRuleGroupFirewallRuleBlockResponse `pulumi:"blockResponse"`
	// ResourceId
	FirewallDomainListId string `pulumi:"firewallDomainListId"`
	// Rule Priority
	Priority int `pulumi:"priority"`
}

// FirewallRuleGroupFirewallRuleInput is an input type that accepts FirewallRuleGroupFirewallRuleArgs and FirewallRuleGroupFirewallRuleOutput values.
// You can construct a concrete instance of `FirewallRuleGroupFirewallRuleInput` via:
//
//          FirewallRuleGroupFirewallRuleArgs{...}
type FirewallRuleGroupFirewallRuleInput interface {
	pulumi.Input

	ToFirewallRuleGroupFirewallRuleOutput() FirewallRuleGroupFirewallRuleOutput
	ToFirewallRuleGroupFirewallRuleOutputWithContext(context.Context) FirewallRuleGroupFirewallRuleOutput
}

// Firewall Rule associating the Rule Group to a Domain List
type FirewallRuleGroupFirewallRuleArgs struct {
	// Rule Action
	Action FirewallRuleGroupFirewallRuleActionInput `pulumi:"action"`
	// BlockOverrideDnsType
	BlockOverrideDnsType FirewallRuleGroupFirewallRuleBlockOverrideDnsTypePtrInput `pulumi:"blockOverrideDnsType"`
	// BlockOverrideDomain
	BlockOverrideDomain pulumi.StringPtrInput `pulumi:"blockOverrideDomain"`
	// BlockOverrideTtl
	BlockOverrideTtl pulumi.IntPtrInput `pulumi:"blockOverrideTtl"`
	// BlockResponse
	BlockResponse FirewallRuleGroupFirewallRuleBlockResponsePtrInput `pulumi:"blockResponse"`
	// ResourceId
	FirewallDomainListId pulumi.StringInput `pulumi:"firewallDomainListId"`
	// Rule Priority
	Priority pulumi.IntInput `pulumi:"priority"`
}

func (FirewallRuleGroupFirewallRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallRuleGroupFirewallRule)(nil)).Elem()
}

func (i FirewallRuleGroupFirewallRuleArgs) ToFirewallRuleGroupFirewallRuleOutput() FirewallRuleGroupFirewallRuleOutput {
	return i.ToFirewallRuleGroupFirewallRuleOutputWithContext(context.Background())
}

func (i FirewallRuleGroupFirewallRuleArgs) ToFirewallRuleGroupFirewallRuleOutputWithContext(ctx context.Context) FirewallRuleGroupFirewallRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleGroupFirewallRuleOutput)
}

// FirewallRuleGroupFirewallRuleArrayInput is an input type that accepts FirewallRuleGroupFirewallRuleArray and FirewallRuleGroupFirewallRuleArrayOutput values.
// You can construct a concrete instance of `FirewallRuleGroupFirewallRuleArrayInput` via:
//
//          FirewallRuleGroupFirewallRuleArray{ FirewallRuleGroupFirewallRuleArgs{...} }
type FirewallRuleGroupFirewallRuleArrayInput interface {
	pulumi.Input

	ToFirewallRuleGroupFirewallRuleArrayOutput() FirewallRuleGroupFirewallRuleArrayOutput
	ToFirewallRuleGroupFirewallRuleArrayOutputWithContext(context.Context) FirewallRuleGroupFirewallRuleArrayOutput
}

type FirewallRuleGroupFirewallRuleArray []FirewallRuleGroupFirewallRuleInput

func (FirewallRuleGroupFirewallRuleArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]FirewallRuleGroupFirewallRule)(nil)).Elem()
}

func (i FirewallRuleGroupFirewallRuleArray) ToFirewallRuleGroupFirewallRuleArrayOutput() FirewallRuleGroupFirewallRuleArrayOutput {
	return i.ToFirewallRuleGroupFirewallRuleArrayOutputWithContext(context.Background())
}

func (i FirewallRuleGroupFirewallRuleArray) ToFirewallRuleGroupFirewallRuleArrayOutputWithContext(ctx context.Context) FirewallRuleGroupFirewallRuleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleGroupFirewallRuleArrayOutput)
}

// Firewall Rule associating the Rule Group to a Domain List
type FirewallRuleGroupFirewallRuleOutput struct{ *pulumi.OutputState }

func (FirewallRuleGroupFirewallRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallRuleGroupFirewallRule)(nil)).Elem()
}

func (o FirewallRuleGroupFirewallRuleOutput) ToFirewallRuleGroupFirewallRuleOutput() FirewallRuleGroupFirewallRuleOutput {
	return o
}

func (o FirewallRuleGroupFirewallRuleOutput) ToFirewallRuleGroupFirewallRuleOutputWithContext(ctx context.Context) FirewallRuleGroupFirewallRuleOutput {
	return o
}

// Rule Action
func (o FirewallRuleGroupFirewallRuleOutput) Action() FirewallRuleGroupFirewallRuleActionOutput {
	return o.ApplyT(func(v FirewallRuleGroupFirewallRule) FirewallRuleGroupFirewallRuleAction { return v.Action }).(FirewallRuleGroupFirewallRuleActionOutput)
}

// BlockOverrideDnsType
func (o FirewallRuleGroupFirewallRuleOutput) BlockOverrideDnsType() FirewallRuleGroupFirewallRuleBlockOverrideDnsTypePtrOutput {
	return o.ApplyT(func(v FirewallRuleGroupFirewallRule) *FirewallRuleGroupFirewallRuleBlockOverrideDnsType {
		return v.BlockOverrideDnsType
	}).(FirewallRuleGroupFirewallRuleBlockOverrideDnsTypePtrOutput)
}

// BlockOverrideDomain
func (o FirewallRuleGroupFirewallRuleOutput) BlockOverrideDomain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v FirewallRuleGroupFirewallRule) *string { return v.BlockOverrideDomain }).(pulumi.StringPtrOutput)
}

// BlockOverrideTtl
func (o FirewallRuleGroupFirewallRuleOutput) BlockOverrideTtl() pulumi.IntPtrOutput {
	return o.ApplyT(func(v FirewallRuleGroupFirewallRule) *int { return v.BlockOverrideTtl }).(pulumi.IntPtrOutput)
}

// BlockResponse
func (o FirewallRuleGroupFirewallRuleOutput) BlockResponse() FirewallRuleGroupFirewallRuleBlockResponsePtrOutput {
	return o.ApplyT(func(v FirewallRuleGroupFirewallRule) *FirewallRuleGroupFirewallRuleBlockResponse {
		return v.BlockResponse
	}).(FirewallRuleGroupFirewallRuleBlockResponsePtrOutput)
}

// ResourceId
func (o FirewallRuleGroupFirewallRuleOutput) FirewallDomainListId() pulumi.StringOutput {
	return o.ApplyT(func(v FirewallRuleGroupFirewallRule) string { return v.FirewallDomainListId }).(pulumi.StringOutput)
}

// Rule Priority
func (o FirewallRuleGroupFirewallRuleOutput) Priority() pulumi.IntOutput {
	return o.ApplyT(func(v FirewallRuleGroupFirewallRule) int { return v.Priority }).(pulumi.IntOutput)
}

type FirewallRuleGroupFirewallRuleArrayOutput struct{ *pulumi.OutputState }

func (FirewallRuleGroupFirewallRuleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]FirewallRuleGroupFirewallRule)(nil)).Elem()
}

func (o FirewallRuleGroupFirewallRuleArrayOutput) ToFirewallRuleGroupFirewallRuleArrayOutput() FirewallRuleGroupFirewallRuleArrayOutput {
	return o
}

func (o FirewallRuleGroupFirewallRuleArrayOutput) ToFirewallRuleGroupFirewallRuleArrayOutputWithContext(ctx context.Context) FirewallRuleGroupFirewallRuleArrayOutput {
	return o
}

func (o FirewallRuleGroupFirewallRuleArrayOutput) Index(i pulumi.IntInput) FirewallRuleGroupFirewallRuleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) FirewallRuleGroupFirewallRule {
		return vs[0].([]FirewallRuleGroupFirewallRule)[vs[1].(int)]
	}).(FirewallRuleGroupFirewallRuleOutput)
}

// A key-value pair to associate with a resource.
type FirewallRuleGroupTag struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key string `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value string `pulumi:"value"`
}

// FirewallRuleGroupTagInput is an input type that accepts FirewallRuleGroupTagArgs and FirewallRuleGroupTagOutput values.
// You can construct a concrete instance of `FirewallRuleGroupTagInput` via:
//
//          FirewallRuleGroupTagArgs{...}
type FirewallRuleGroupTagInput interface {
	pulumi.Input

	ToFirewallRuleGroupTagOutput() FirewallRuleGroupTagOutput
	ToFirewallRuleGroupTagOutputWithContext(context.Context) FirewallRuleGroupTagOutput
}

// A key-value pair to associate with a resource.
type FirewallRuleGroupTagArgs struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key pulumi.StringInput `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value pulumi.StringInput `pulumi:"value"`
}

func (FirewallRuleGroupTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallRuleGroupTag)(nil)).Elem()
}

func (i FirewallRuleGroupTagArgs) ToFirewallRuleGroupTagOutput() FirewallRuleGroupTagOutput {
	return i.ToFirewallRuleGroupTagOutputWithContext(context.Background())
}

func (i FirewallRuleGroupTagArgs) ToFirewallRuleGroupTagOutputWithContext(ctx context.Context) FirewallRuleGroupTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleGroupTagOutput)
}

// FirewallRuleGroupTagArrayInput is an input type that accepts FirewallRuleGroupTagArray and FirewallRuleGroupTagArrayOutput values.
// You can construct a concrete instance of `FirewallRuleGroupTagArrayInput` via:
//
//          FirewallRuleGroupTagArray{ FirewallRuleGroupTagArgs{...} }
type FirewallRuleGroupTagArrayInput interface {
	pulumi.Input

	ToFirewallRuleGroupTagArrayOutput() FirewallRuleGroupTagArrayOutput
	ToFirewallRuleGroupTagArrayOutputWithContext(context.Context) FirewallRuleGroupTagArrayOutput
}

type FirewallRuleGroupTagArray []FirewallRuleGroupTagInput

func (FirewallRuleGroupTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]FirewallRuleGroupTag)(nil)).Elem()
}

func (i FirewallRuleGroupTagArray) ToFirewallRuleGroupTagArrayOutput() FirewallRuleGroupTagArrayOutput {
	return i.ToFirewallRuleGroupTagArrayOutputWithContext(context.Background())
}

func (i FirewallRuleGroupTagArray) ToFirewallRuleGroupTagArrayOutputWithContext(ctx context.Context) FirewallRuleGroupTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleGroupTagArrayOutput)
}

// A key-value pair to associate with a resource.
type FirewallRuleGroupTagOutput struct{ *pulumi.OutputState }

func (FirewallRuleGroupTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallRuleGroupTag)(nil)).Elem()
}

func (o FirewallRuleGroupTagOutput) ToFirewallRuleGroupTagOutput() FirewallRuleGroupTagOutput {
	return o
}

func (o FirewallRuleGroupTagOutput) ToFirewallRuleGroupTagOutputWithContext(ctx context.Context) FirewallRuleGroupTagOutput {
	return o
}

// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o FirewallRuleGroupTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v FirewallRuleGroupTag) string { return v.Key }).(pulumi.StringOutput)
}

// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o FirewallRuleGroupTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v FirewallRuleGroupTag) string { return v.Value }).(pulumi.StringOutput)
}

type FirewallRuleGroupTagArrayOutput struct{ *pulumi.OutputState }

func (FirewallRuleGroupTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]FirewallRuleGroupTag)(nil)).Elem()
}

func (o FirewallRuleGroupTagArrayOutput) ToFirewallRuleGroupTagArrayOutput() FirewallRuleGroupTagArrayOutput {
	return o
}

func (o FirewallRuleGroupTagArrayOutput) ToFirewallRuleGroupTagArrayOutputWithContext(ctx context.Context) FirewallRuleGroupTagArrayOutput {
	return o
}

func (o FirewallRuleGroupTagArrayOutput) Index(i pulumi.IntInput) FirewallRuleGroupTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) FirewallRuleGroupTag {
		return vs[0].([]FirewallRuleGroupTag)[vs[1].(int)]
	}).(FirewallRuleGroupTagOutput)
}

func init() {
	pulumi.RegisterOutputType(FirewallDomainListTagOutput{})
	pulumi.RegisterOutputType(FirewallDomainListTagArrayOutput{})
	pulumi.RegisterOutputType(FirewallRuleGroupAssociationTagOutput{})
	pulumi.RegisterOutputType(FirewallRuleGroupAssociationTagArrayOutput{})
	pulumi.RegisterOutputType(FirewallRuleGroupFirewallRuleOutput{})
	pulumi.RegisterOutputType(FirewallRuleGroupFirewallRuleArrayOutput{})
	pulumi.RegisterOutputType(FirewallRuleGroupTagOutput{})
	pulumi.RegisterOutputType(FirewallRuleGroupTagArrayOutput{})
}
