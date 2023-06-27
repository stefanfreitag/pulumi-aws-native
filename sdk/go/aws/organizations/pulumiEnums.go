// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package organizations

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The method by which the account joined the organization.
type AccountJoinedMethod string

const (
	AccountJoinedMethodInvited = AccountJoinedMethod("INVITED")
	AccountJoinedMethodCreated = AccountJoinedMethod("CREATED")
)

type AccountJoinedMethodOutput struct{ *pulumi.OutputState }

func (AccountJoinedMethodOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AccountJoinedMethod)(nil)).Elem()
}

func (o AccountJoinedMethodOutput) ToAccountJoinedMethodOutput() AccountJoinedMethodOutput {
	return o
}

func (o AccountJoinedMethodOutput) ToAccountJoinedMethodOutputWithContext(ctx context.Context) AccountJoinedMethodOutput {
	return o
}

func (o AccountJoinedMethodOutput) ToAccountJoinedMethodPtrOutput() AccountJoinedMethodPtrOutput {
	return o.ToAccountJoinedMethodPtrOutputWithContext(context.Background())
}

func (o AccountJoinedMethodOutput) ToAccountJoinedMethodPtrOutputWithContext(ctx context.Context) AccountJoinedMethodPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AccountJoinedMethod) *AccountJoinedMethod {
		return &v
	}).(AccountJoinedMethodPtrOutput)
}

func (o AccountJoinedMethodOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AccountJoinedMethodOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AccountJoinedMethod) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AccountJoinedMethodOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AccountJoinedMethodOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AccountJoinedMethod) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AccountJoinedMethodPtrOutput struct{ *pulumi.OutputState }

func (AccountJoinedMethodPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AccountJoinedMethod)(nil)).Elem()
}

func (o AccountJoinedMethodPtrOutput) ToAccountJoinedMethodPtrOutput() AccountJoinedMethodPtrOutput {
	return o
}

func (o AccountJoinedMethodPtrOutput) ToAccountJoinedMethodPtrOutputWithContext(ctx context.Context) AccountJoinedMethodPtrOutput {
	return o
}

func (o AccountJoinedMethodPtrOutput) Elem() AccountJoinedMethodOutput {
	return o.ApplyT(func(v *AccountJoinedMethod) AccountJoinedMethod {
		if v != nil {
			return *v
		}
		var ret AccountJoinedMethod
		return ret
	}).(AccountJoinedMethodOutput)
}

func (o AccountJoinedMethodPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AccountJoinedMethodPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AccountJoinedMethod) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// The status of the account in the organization.
type AccountStatus string

const (
	AccountStatusActive         = AccountStatus("ACTIVE")
	AccountStatusSuspended      = AccountStatus("SUSPENDED")
	AccountStatusPendingClosure = AccountStatus("PENDING_CLOSURE")
)

type AccountStatusOutput struct{ *pulumi.OutputState }

func (AccountStatusOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AccountStatus)(nil)).Elem()
}

func (o AccountStatusOutput) ToAccountStatusOutput() AccountStatusOutput {
	return o
}

func (o AccountStatusOutput) ToAccountStatusOutputWithContext(ctx context.Context) AccountStatusOutput {
	return o
}

func (o AccountStatusOutput) ToAccountStatusPtrOutput() AccountStatusPtrOutput {
	return o.ToAccountStatusPtrOutputWithContext(context.Background())
}

func (o AccountStatusOutput) ToAccountStatusPtrOutputWithContext(ctx context.Context) AccountStatusPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AccountStatus) *AccountStatus {
		return &v
	}).(AccountStatusPtrOutput)
}

func (o AccountStatusOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AccountStatusOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AccountStatus) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AccountStatusOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AccountStatusOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AccountStatus) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AccountStatusPtrOutput struct{ *pulumi.OutputState }

func (AccountStatusPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AccountStatus)(nil)).Elem()
}

func (o AccountStatusPtrOutput) ToAccountStatusPtrOutput() AccountStatusPtrOutput {
	return o
}

func (o AccountStatusPtrOutput) ToAccountStatusPtrOutputWithContext(ctx context.Context) AccountStatusPtrOutput {
	return o
}

func (o AccountStatusPtrOutput) Elem() AccountStatusOutput {
	return o.ApplyT(func(v *AccountStatus) AccountStatus {
		if v != nil {
			return *v
		}
		var ret AccountStatus
		return ret
	}).(AccountStatusOutput)
}

func (o AccountStatusPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AccountStatusPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AccountStatus) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.
type OrganizationFeatureSet string

const (
	OrganizationFeatureSetAll                 = OrganizationFeatureSet("ALL")
	OrganizationFeatureSetConsolidatedBilling = OrganizationFeatureSet("CONSOLIDATED_BILLING")
)

func (OrganizationFeatureSet) ElementType() reflect.Type {
	return reflect.TypeOf((*OrganizationFeatureSet)(nil)).Elem()
}

func (e OrganizationFeatureSet) ToOrganizationFeatureSetOutput() OrganizationFeatureSetOutput {
	return pulumi.ToOutput(e).(OrganizationFeatureSetOutput)
}

func (e OrganizationFeatureSet) ToOrganizationFeatureSetOutputWithContext(ctx context.Context) OrganizationFeatureSetOutput {
	return pulumi.ToOutputWithContext(ctx, e).(OrganizationFeatureSetOutput)
}

func (e OrganizationFeatureSet) ToOrganizationFeatureSetPtrOutput() OrganizationFeatureSetPtrOutput {
	return e.ToOrganizationFeatureSetPtrOutputWithContext(context.Background())
}

func (e OrganizationFeatureSet) ToOrganizationFeatureSetPtrOutputWithContext(ctx context.Context) OrganizationFeatureSetPtrOutput {
	return OrganizationFeatureSet(e).ToOrganizationFeatureSetOutputWithContext(ctx).ToOrganizationFeatureSetPtrOutputWithContext(ctx)
}

func (e OrganizationFeatureSet) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e OrganizationFeatureSet) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e OrganizationFeatureSet) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e OrganizationFeatureSet) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type OrganizationFeatureSetOutput struct{ *pulumi.OutputState }

func (OrganizationFeatureSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*OrganizationFeatureSet)(nil)).Elem()
}

func (o OrganizationFeatureSetOutput) ToOrganizationFeatureSetOutput() OrganizationFeatureSetOutput {
	return o
}

func (o OrganizationFeatureSetOutput) ToOrganizationFeatureSetOutputWithContext(ctx context.Context) OrganizationFeatureSetOutput {
	return o
}

func (o OrganizationFeatureSetOutput) ToOrganizationFeatureSetPtrOutput() OrganizationFeatureSetPtrOutput {
	return o.ToOrganizationFeatureSetPtrOutputWithContext(context.Background())
}

func (o OrganizationFeatureSetOutput) ToOrganizationFeatureSetPtrOutputWithContext(ctx context.Context) OrganizationFeatureSetPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v OrganizationFeatureSet) *OrganizationFeatureSet {
		return &v
	}).(OrganizationFeatureSetPtrOutput)
}

func (o OrganizationFeatureSetOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o OrganizationFeatureSetOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e OrganizationFeatureSet) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o OrganizationFeatureSetOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o OrganizationFeatureSetOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e OrganizationFeatureSet) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type OrganizationFeatureSetPtrOutput struct{ *pulumi.OutputState }

func (OrganizationFeatureSetPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OrganizationFeatureSet)(nil)).Elem()
}

func (o OrganizationFeatureSetPtrOutput) ToOrganizationFeatureSetPtrOutput() OrganizationFeatureSetPtrOutput {
	return o
}

func (o OrganizationFeatureSetPtrOutput) ToOrganizationFeatureSetPtrOutputWithContext(ctx context.Context) OrganizationFeatureSetPtrOutput {
	return o
}

func (o OrganizationFeatureSetPtrOutput) Elem() OrganizationFeatureSetOutput {
	return o.ApplyT(func(v *OrganizationFeatureSet) OrganizationFeatureSet {
		if v != nil {
			return *v
		}
		var ret OrganizationFeatureSet
		return ret
	}).(OrganizationFeatureSetOutput)
}

func (o OrganizationFeatureSetPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o OrganizationFeatureSetPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *OrganizationFeatureSet) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// OrganizationFeatureSetInput is an input type that accepts OrganizationFeatureSetArgs and OrganizationFeatureSetOutput values.
// You can construct a concrete instance of `OrganizationFeatureSetInput` via:
//
//	OrganizationFeatureSetArgs{...}
type OrganizationFeatureSetInput interface {
	pulumi.Input

	ToOrganizationFeatureSetOutput() OrganizationFeatureSetOutput
	ToOrganizationFeatureSetOutputWithContext(context.Context) OrganizationFeatureSetOutput
}

var organizationFeatureSetPtrType = reflect.TypeOf((**OrganizationFeatureSet)(nil)).Elem()

type OrganizationFeatureSetPtrInput interface {
	pulumi.Input

	ToOrganizationFeatureSetPtrOutput() OrganizationFeatureSetPtrOutput
	ToOrganizationFeatureSetPtrOutputWithContext(context.Context) OrganizationFeatureSetPtrOutput
}

type organizationFeatureSetPtr string

func OrganizationFeatureSetPtr(v string) OrganizationFeatureSetPtrInput {
	return (*organizationFeatureSetPtr)(&v)
}

func (*organizationFeatureSetPtr) ElementType() reflect.Type {
	return organizationFeatureSetPtrType
}

func (in *organizationFeatureSetPtr) ToOrganizationFeatureSetPtrOutput() OrganizationFeatureSetPtrOutput {
	return pulumi.ToOutput(in).(OrganizationFeatureSetPtrOutput)
}

func (in *organizationFeatureSetPtr) ToOrganizationFeatureSetPtrOutputWithContext(ctx context.Context) OrganizationFeatureSetPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(OrganizationFeatureSetPtrOutput)
}

// The type of policy to create. You can specify one of the following values: AISERVICES_OPT_OUT_POLICY, BACKUP_POLICY, SERVICE_CONTROL_POLICY, TAG_POLICY
type PolicyType string

const (
	PolicyTypeServiceControlPolicy   = PolicyType("SERVICE_CONTROL_POLICY")
	PolicyTypeAiservicesOptOutPolicy = PolicyType("AISERVICES_OPT_OUT_POLICY")
	PolicyTypeBackupPolicy           = PolicyType("BACKUP_POLICY")
	PolicyTypeTagPolicy              = PolicyType("TAG_POLICY")
)

func (PolicyType) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyType)(nil)).Elem()
}

func (e PolicyType) ToPolicyTypeOutput() PolicyTypeOutput {
	return pulumi.ToOutput(e).(PolicyTypeOutput)
}

func (e PolicyType) ToPolicyTypeOutputWithContext(ctx context.Context) PolicyTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(PolicyTypeOutput)
}

func (e PolicyType) ToPolicyTypePtrOutput() PolicyTypePtrOutput {
	return e.ToPolicyTypePtrOutputWithContext(context.Background())
}

func (e PolicyType) ToPolicyTypePtrOutputWithContext(ctx context.Context) PolicyTypePtrOutput {
	return PolicyType(e).ToPolicyTypeOutputWithContext(ctx).ToPolicyTypePtrOutputWithContext(ctx)
}

func (e PolicyType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e PolicyType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e PolicyType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e PolicyType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type PolicyTypeOutput struct{ *pulumi.OutputState }

func (PolicyTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PolicyType)(nil)).Elem()
}

func (o PolicyTypeOutput) ToPolicyTypeOutput() PolicyTypeOutput {
	return o
}

func (o PolicyTypeOutput) ToPolicyTypeOutputWithContext(ctx context.Context) PolicyTypeOutput {
	return o
}

func (o PolicyTypeOutput) ToPolicyTypePtrOutput() PolicyTypePtrOutput {
	return o.ToPolicyTypePtrOutputWithContext(context.Background())
}

func (o PolicyTypeOutput) ToPolicyTypePtrOutputWithContext(ctx context.Context) PolicyTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v PolicyType) *PolicyType {
		return &v
	}).(PolicyTypePtrOutput)
}

func (o PolicyTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o PolicyTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e PolicyType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o PolicyTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o PolicyTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e PolicyType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type PolicyTypePtrOutput struct{ *pulumi.OutputState }

func (PolicyTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PolicyType)(nil)).Elem()
}

func (o PolicyTypePtrOutput) ToPolicyTypePtrOutput() PolicyTypePtrOutput {
	return o
}

func (o PolicyTypePtrOutput) ToPolicyTypePtrOutputWithContext(ctx context.Context) PolicyTypePtrOutput {
	return o
}

func (o PolicyTypePtrOutput) Elem() PolicyTypeOutput {
	return o.ApplyT(func(v *PolicyType) PolicyType {
		if v != nil {
			return *v
		}
		var ret PolicyType
		return ret
	}).(PolicyTypeOutput)
}

func (o PolicyTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o PolicyTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *PolicyType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// PolicyTypeInput is an input type that accepts PolicyTypeArgs and PolicyTypeOutput values.
// You can construct a concrete instance of `PolicyTypeInput` via:
//
//	PolicyTypeArgs{...}
type PolicyTypeInput interface {
	pulumi.Input

	ToPolicyTypeOutput() PolicyTypeOutput
	ToPolicyTypeOutputWithContext(context.Context) PolicyTypeOutput
}

var policyTypePtrType = reflect.TypeOf((**PolicyType)(nil)).Elem()

type PolicyTypePtrInput interface {
	pulumi.Input

	ToPolicyTypePtrOutput() PolicyTypePtrOutput
	ToPolicyTypePtrOutputWithContext(context.Context) PolicyTypePtrOutput
}

type policyTypePtr string

func PolicyTypePtr(v string) PolicyTypePtrInput {
	return (*policyTypePtr)(&v)
}

func (*policyTypePtr) ElementType() reflect.Type {
	return policyTypePtrType
}

func (in *policyTypePtr) ToPolicyTypePtrOutput() PolicyTypePtrOutput {
	return pulumi.ToOutput(in).(PolicyTypePtrOutput)
}

func (in *policyTypePtr) ToPolicyTypePtrOutputWithContext(ctx context.Context) PolicyTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(PolicyTypePtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationFeatureSetInput)(nil)).Elem(), OrganizationFeatureSet("ALL"))
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationFeatureSetPtrInput)(nil)).Elem(), OrganizationFeatureSet("ALL"))
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyTypeInput)(nil)).Elem(), PolicyType("SERVICE_CONTROL_POLICY"))
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyTypePtrInput)(nil)).Elem(), PolicyType("SERVICE_CONTROL_POLICY"))
	pulumi.RegisterOutputType(AccountJoinedMethodOutput{})
	pulumi.RegisterOutputType(AccountJoinedMethodPtrOutput{})
	pulumi.RegisterOutputType(AccountStatusOutput{})
	pulumi.RegisterOutputType(AccountStatusPtrOutput{})
	pulumi.RegisterOutputType(OrganizationFeatureSetOutput{})
	pulumi.RegisterOutputType(OrganizationFeatureSetPtrOutput{})
	pulumi.RegisterOutputType(PolicyTypeOutput{})
	pulumi.RegisterOutputType(PolicyTypePtrOutput{})
}
