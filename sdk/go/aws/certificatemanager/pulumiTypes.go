// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package certificatemanager

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type AccountExpiryEventsConfiguration struct {
	DaysBeforeExpiry *int `pulumi:"daysBeforeExpiry"`
}

// AccountExpiryEventsConfigurationInput is an input type that accepts AccountExpiryEventsConfigurationArgs and AccountExpiryEventsConfigurationOutput values.
// You can construct a concrete instance of `AccountExpiryEventsConfigurationInput` via:
//
//          AccountExpiryEventsConfigurationArgs{...}
type AccountExpiryEventsConfigurationInput interface {
	pulumi.Input

	ToAccountExpiryEventsConfigurationOutput() AccountExpiryEventsConfigurationOutput
	ToAccountExpiryEventsConfigurationOutputWithContext(context.Context) AccountExpiryEventsConfigurationOutput
}

type AccountExpiryEventsConfigurationArgs struct {
	DaysBeforeExpiry pulumi.IntPtrInput `pulumi:"daysBeforeExpiry"`
}

func (AccountExpiryEventsConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AccountExpiryEventsConfiguration)(nil)).Elem()
}

func (i AccountExpiryEventsConfigurationArgs) ToAccountExpiryEventsConfigurationOutput() AccountExpiryEventsConfigurationOutput {
	return i.ToAccountExpiryEventsConfigurationOutputWithContext(context.Background())
}

func (i AccountExpiryEventsConfigurationArgs) ToAccountExpiryEventsConfigurationOutputWithContext(ctx context.Context) AccountExpiryEventsConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccountExpiryEventsConfigurationOutput)
}

func (i AccountExpiryEventsConfigurationArgs) ToAccountExpiryEventsConfigurationPtrOutput() AccountExpiryEventsConfigurationPtrOutput {
	return i.ToAccountExpiryEventsConfigurationPtrOutputWithContext(context.Background())
}

func (i AccountExpiryEventsConfigurationArgs) ToAccountExpiryEventsConfigurationPtrOutputWithContext(ctx context.Context) AccountExpiryEventsConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccountExpiryEventsConfigurationOutput).ToAccountExpiryEventsConfigurationPtrOutputWithContext(ctx)
}

// AccountExpiryEventsConfigurationPtrInput is an input type that accepts AccountExpiryEventsConfigurationArgs, AccountExpiryEventsConfigurationPtr and AccountExpiryEventsConfigurationPtrOutput values.
// You can construct a concrete instance of `AccountExpiryEventsConfigurationPtrInput` via:
//
//          AccountExpiryEventsConfigurationArgs{...}
//
//  or:
//
//          nil
type AccountExpiryEventsConfigurationPtrInput interface {
	pulumi.Input

	ToAccountExpiryEventsConfigurationPtrOutput() AccountExpiryEventsConfigurationPtrOutput
	ToAccountExpiryEventsConfigurationPtrOutputWithContext(context.Context) AccountExpiryEventsConfigurationPtrOutput
}

type accountExpiryEventsConfigurationPtrType AccountExpiryEventsConfigurationArgs

func AccountExpiryEventsConfigurationPtr(v *AccountExpiryEventsConfigurationArgs) AccountExpiryEventsConfigurationPtrInput {
	return (*accountExpiryEventsConfigurationPtrType)(v)
}

func (*accountExpiryEventsConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AccountExpiryEventsConfiguration)(nil)).Elem()
}

func (i *accountExpiryEventsConfigurationPtrType) ToAccountExpiryEventsConfigurationPtrOutput() AccountExpiryEventsConfigurationPtrOutput {
	return i.ToAccountExpiryEventsConfigurationPtrOutputWithContext(context.Background())
}

func (i *accountExpiryEventsConfigurationPtrType) ToAccountExpiryEventsConfigurationPtrOutputWithContext(ctx context.Context) AccountExpiryEventsConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccountExpiryEventsConfigurationPtrOutput)
}

type AccountExpiryEventsConfigurationOutput struct{ *pulumi.OutputState }

func (AccountExpiryEventsConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AccountExpiryEventsConfiguration)(nil)).Elem()
}

func (o AccountExpiryEventsConfigurationOutput) ToAccountExpiryEventsConfigurationOutput() AccountExpiryEventsConfigurationOutput {
	return o
}

func (o AccountExpiryEventsConfigurationOutput) ToAccountExpiryEventsConfigurationOutputWithContext(ctx context.Context) AccountExpiryEventsConfigurationOutput {
	return o
}

func (o AccountExpiryEventsConfigurationOutput) ToAccountExpiryEventsConfigurationPtrOutput() AccountExpiryEventsConfigurationPtrOutput {
	return o.ToAccountExpiryEventsConfigurationPtrOutputWithContext(context.Background())
}

func (o AccountExpiryEventsConfigurationOutput) ToAccountExpiryEventsConfigurationPtrOutputWithContext(ctx context.Context) AccountExpiryEventsConfigurationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AccountExpiryEventsConfiguration) *AccountExpiryEventsConfiguration {
		return &v
	}).(AccountExpiryEventsConfigurationPtrOutput)
}

func (o AccountExpiryEventsConfigurationOutput) DaysBeforeExpiry() pulumi.IntPtrOutput {
	return o.ApplyT(func(v AccountExpiryEventsConfiguration) *int { return v.DaysBeforeExpiry }).(pulumi.IntPtrOutput)
}

type AccountExpiryEventsConfigurationPtrOutput struct{ *pulumi.OutputState }

func (AccountExpiryEventsConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AccountExpiryEventsConfiguration)(nil)).Elem()
}

func (o AccountExpiryEventsConfigurationPtrOutput) ToAccountExpiryEventsConfigurationPtrOutput() AccountExpiryEventsConfigurationPtrOutput {
	return o
}

func (o AccountExpiryEventsConfigurationPtrOutput) ToAccountExpiryEventsConfigurationPtrOutputWithContext(ctx context.Context) AccountExpiryEventsConfigurationPtrOutput {
	return o
}

func (o AccountExpiryEventsConfigurationPtrOutput) Elem() AccountExpiryEventsConfigurationOutput {
	return o.ApplyT(func(v *AccountExpiryEventsConfiguration) AccountExpiryEventsConfiguration {
		if v != nil {
			return *v
		}
		var ret AccountExpiryEventsConfiguration
		return ret
	}).(AccountExpiryEventsConfigurationOutput)
}

func (o AccountExpiryEventsConfigurationPtrOutput) DaysBeforeExpiry() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *AccountExpiryEventsConfiguration) *int {
		if v == nil {
			return nil
		}
		return v.DaysBeforeExpiry
	}).(pulumi.IntPtrOutput)
}

type CertificateDomainValidationOption struct {
	DomainName       string  `pulumi:"domainName"`
	HostedZoneId     *string `pulumi:"hostedZoneId"`
	ValidationDomain *string `pulumi:"validationDomain"`
}

// CertificateDomainValidationOptionInput is an input type that accepts CertificateDomainValidationOptionArgs and CertificateDomainValidationOptionOutput values.
// You can construct a concrete instance of `CertificateDomainValidationOptionInput` via:
//
//          CertificateDomainValidationOptionArgs{...}
type CertificateDomainValidationOptionInput interface {
	pulumi.Input

	ToCertificateDomainValidationOptionOutput() CertificateDomainValidationOptionOutput
	ToCertificateDomainValidationOptionOutputWithContext(context.Context) CertificateDomainValidationOptionOutput
}

type CertificateDomainValidationOptionArgs struct {
	DomainName       pulumi.StringInput    `pulumi:"domainName"`
	HostedZoneId     pulumi.StringPtrInput `pulumi:"hostedZoneId"`
	ValidationDomain pulumi.StringPtrInput `pulumi:"validationDomain"`
}

func (CertificateDomainValidationOptionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificateDomainValidationOption)(nil)).Elem()
}

func (i CertificateDomainValidationOptionArgs) ToCertificateDomainValidationOptionOutput() CertificateDomainValidationOptionOutput {
	return i.ToCertificateDomainValidationOptionOutputWithContext(context.Background())
}

func (i CertificateDomainValidationOptionArgs) ToCertificateDomainValidationOptionOutputWithContext(ctx context.Context) CertificateDomainValidationOptionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateDomainValidationOptionOutput)
}

// CertificateDomainValidationOptionArrayInput is an input type that accepts CertificateDomainValidationOptionArray and CertificateDomainValidationOptionArrayOutput values.
// You can construct a concrete instance of `CertificateDomainValidationOptionArrayInput` via:
//
//          CertificateDomainValidationOptionArray{ CertificateDomainValidationOptionArgs{...} }
type CertificateDomainValidationOptionArrayInput interface {
	pulumi.Input

	ToCertificateDomainValidationOptionArrayOutput() CertificateDomainValidationOptionArrayOutput
	ToCertificateDomainValidationOptionArrayOutputWithContext(context.Context) CertificateDomainValidationOptionArrayOutput
}

type CertificateDomainValidationOptionArray []CertificateDomainValidationOptionInput

func (CertificateDomainValidationOptionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]CertificateDomainValidationOption)(nil)).Elem()
}

func (i CertificateDomainValidationOptionArray) ToCertificateDomainValidationOptionArrayOutput() CertificateDomainValidationOptionArrayOutput {
	return i.ToCertificateDomainValidationOptionArrayOutputWithContext(context.Background())
}

func (i CertificateDomainValidationOptionArray) ToCertificateDomainValidationOptionArrayOutputWithContext(ctx context.Context) CertificateDomainValidationOptionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateDomainValidationOptionArrayOutput)
}

type CertificateDomainValidationOptionOutput struct{ *pulumi.OutputState }

func (CertificateDomainValidationOptionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificateDomainValidationOption)(nil)).Elem()
}

func (o CertificateDomainValidationOptionOutput) ToCertificateDomainValidationOptionOutput() CertificateDomainValidationOptionOutput {
	return o
}

func (o CertificateDomainValidationOptionOutput) ToCertificateDomainValidationOptionOutputWithContext(ctx context.Context) CertificateDomainValidationOptionOutput {
	return o
}

func (o CertificateDomainValidationOptionOutput) DomainName() pulumi.StringOutput {
	return o.ApplyT(func(v CertificateDomainValidationOption) string { return v.DomainName }).(pulumi.StringOutput)
}

func (o CertificateDomainValidationOptionOutput) HostedZoneId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v CertificateDomainValidationOption) *string { return v.HostedZoneId }).(pulumi.StringPtrOutput)
}

func (o CertificateDomainValidationOptionOutput) ValidationDomain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v CertificateDomainValidationOption) *string { return v.ValidationDomain }).(pulumi.StringPtrOutput)
}

type CertificateDomainValidationOptionArrayOutput struct{ *pulumi.OutputState }

func (CertificateDomainValidationOptionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]CertificateDomainValidationOption)(nil)).Elem()
}

func (o CertificateDomainValidationOptionArrayOutput) ToCertificateDomainValidationOptionArrayOutput() CertificateDomainValidationOptionArrayOutput {
	return o
}

func (o CertificateDomainValidationOptionArrayOutput) ToCertificateDomainValidationOptionArrayOutputWithContext(ctx context.Context) CertificateDomainValidationOptionArrayOutput {
	return o
}

func (o CertificateDomainValidationOptionArrayOutput) Index(i pulumi.IntInput) CertificateDomainValidationOptionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) CertificateDomainValidationOption {
		return vs[0].([]CertificateDomainValidationOption)[vs[1].(int)]
	}).(CertificateDomainValidationOptionOutput)
}

type CertificateTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// CertificateTagInput is an input type that accepts CertificateTagArgs and CertificateTagOutput values.
// You can construct a concrete instance of `CertificateTagInput` via:
//
//          CertificateTagArgs{...}
type CertificateTagInput interface {
	pulumi.Input

	ToCertificateTagOutput() CertificateTagOutput
	ToCertificateTagOutputWithContext(context.Context) CertificateTagOutput
}

type CertificateTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (CertificateTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificateTag)(nil)).Elem()
}

func (i CertificateTagArgs) ToCertificateTagOutput() CertificateTagOutput {
	return i.ToCertificateTagOutputWithContext(context.Background())
}

func (i CertificateTagArgs) ToCertificateTagOutputWithContext(ctx context.Context) CertificateTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateTagOutput)
}

// CertificateTagArrayInput is an input type that accepts CertificateTagArray and CertificateTagArrayOutput values.
// You can construct a concrete instance of `CertificateTagArrayInput` via:
//
//          CertificateTagArray{ CertificateTagArgs{...} }
type CertificateTagArrayInput interface {
	pulumi.Input

	ToCertificateTagArrayOutput() CertificateTagArrayOutput
	ToCertificateTagArrayOutputWithContext(context.Context) CertificateTagArrayOutput
}

type CertificateTagArray []CertificateTagInput

func (CertificateTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]CertificateTag)(nil)).Elem()
}

func (i CertificateTagArray) ToCertificateTagArrayOutput() CertificateTagArrayOutput {
	return i.ToCertificateTagArrayOutputWithContext(context.Background())
}

func (i CertificateTagArray) ToCertificateTagArrayOutputWithContext(ctx context.Context) CertificateTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateTagArrayOutput)
}

type CertificateTagOutput struct{ *pulumi.OutputState }

func (CertificateTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificateTag)(nil)).Elem()
}

func (o CertificateTagOutput) ToCertificateTagOutput() CertificateTagOutput {
	return o
}

func (o CertificateTagOutput) ToCertificateTagOutputWithContext(ctx context.Context) CertificateTagOutput {
	return o
}

func (o CertificateTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v CertificateTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o CertificateTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v CertificateTag) string { return v.Value }).(pulumi.StringOutput)
}

type CertificateTagArrayOutput struct{ *pulumi.OutputState }

func (CertificateTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]CertificateTag)(nil)).Elem()
}

func (o CertificateTagArrayOutput) ToCertificateTagArrayOutput() CertificateTagArrayOutput {
	return o
}

func (o CertificateTagArrayOutput) ToCertificateTagArrayOutputWithContext(ctx context.Context) CertificateTagArrayOutput {
	return o
}

func (o CertificateTagArrayOutput) Index(i pulumi.IntInput) CertificateTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) CertificateTag {
		return vs[0].([]CertificateTag)[vs[1].(int)]
	}).(CertificateTagOutput)
}

func init() {
	pulumi.RegisterOutputType(AccountExpiryEventsConfigurationOutput{})
	pulumi.RegisterOutputType(AccountExpiryEventsConfigurationPtrOutput{})
	pulumi.RegisterOutputType(CertificateDomainValidationOptionOutput{})
	pulumi.RegisterOutputType(CertificateDomainValidationOptionArrayOutput{})
	pulumi.RegisterOutputType(CertificateTagOutput{})
	pulumi.RegisterOutputType(CertificateTagArrayOutput{})
}
