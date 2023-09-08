// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package macie

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The status for the AllowList
type AllowListStatus string

const (
	AllowListStatusOk                   = AllowListStatus("OK")
	AllowListStatusS3ObjectNotFound     = AllowListStatus("S3_OBJECT_NOT_FOUND")
	AllowListStatusS3UserAccessDenied   = AllowListStatus("S3_USER_ACCESS_DENIED")
	AllowListStatusS3ObjectAccessDenied = AllowListStatus("S3_OBJECT_ACCESS_DENIED")
	AllowListStatusS3Throttled          = AllowListStatus("S3_THROTTLED")
	AllowListStatusS3ObjectOversize     = AllowListStatus("S3_OBJECT_OVERSIZE")
	AllowListStatusS3ObjectEmpty        = AllowListStatus("S3_OBJECT_EMPTY")
	AllowListStatusUnknownError         = AllowListStatus("UNKNOWN_ERROR")
)

type AllowListStatusOutput struct{ *pulumi.OutputState }

func (AllowListStatusOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AllowListStatus)(nil)).Elem()
}

func (o AllowListStatusOutput) ToAllowListStatusOutput() AllowListStatusOutput {
	return o
}

func (o AllowListStatusOutput) ToAllowListStatusOutputWithContext(ctx context.Context) AllowListStatusOutput {
	return o
}

func (o AllowListStatusOutput) ToAllowListStatusPtrOutput() AllowListStatusPtrOutput {
	return o.ToAllowListStatusPtrOutputWithContext(context.Background())
}

func (o AllowListStatusOutput) ToAllowListStatusPtrOutputWithContext(ctx context.Context) AllowListStatusPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AllowListStatus) *AllowListStatus {
		return &v
	}).(AllowListStatusPtrOutput)
}

func (o AllowListStatusOutput) ToOutput(ctx context.Context) pulumix.Output[AllowListStatus] {
	return pulumix.Output[AllowListStatus]{
		OutputState: o.OutputState,
	}
}

func (o AllowListStatusOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AllowListStatusOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AllowListStatus) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AllowListStatusOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AllowListStatusOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AllowListStatus) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AllowListStatusPtrOutput struct{ *pulumi.OutputState }

func (AllowListStatusPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AllowListStatus)(nil)).Elem()
}

func (o AllowListStatusPtrOutput) ToAllowListStatusPtrOutput() AllowListStatusPtrOutput {
	return o
}

func (o AllowListStatusPtrOutput) ToAllowListStatusPtrOutputWithContext(ctx context.Context) AllowListStatusPtrOutput {
	return o
}

func (o AllowListStatusPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*AllowListStatus] {
	return pulumix.Output[*AllowListStatus]{
		OutputState: o.OutputState,
	}
}

func (o AllowListStatusPtrOutput) Elem() AllowListStatusOutput {
	return o.ApplyT(func(v *AllowListStatus) AllowListStatus {
		if v != nil {
			return *v
		}
		var ret AllowListStatus
		return ret
	}).(AllowListStatusOutput)
}

func (o AllowListStatusPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AllowListStatusPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AllowListStatus) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type FindingsFilterFindingFilterAction string

const (
	FindingsFilterFindingFilterActionArchive = FindingsFilterFindingFilterAction("ARCHIVE")
	FindingsFilterFindingFilterActionNoop    = FindingsFilterFindingFilterAction("NOOP")
)

func (FindingsFilterFindingFilterAction) ElementType() reflect.Type {
	return reflect.TypeOf((*FindingsFilterFindingFilterAction)(nil)).Elem()
}

func (e FindingsFilterFindingFilterAction) ToFindingsFilterFindingFilterActionOutput() FindingsFilterFindingFilterActionOutput {
	return pulumi.ToOutput(e).(FindingsFilterFindingFilterActionOutput)
}

func (e FindingsFilterFindingFilterAction) ToFindingsFilterFindingFilterActionOutputWithContext(ctx context.Context) FindingsFilterFindingFilterActionOutput {
	return pulumi.ToOutputWithContext(ctx, e).(FindingsFilterFindingFilterActionOutput)
}

func (e FindingsFilterFindingFilterAction) ToFindingsFilterFindingFilterActionPtrOutput() FindingsFilterFindingFilterActionPtrOutput {
	return e.ToFindingsFilterFindingFilterActionPtrOutputWithContext(context.Background())
}

func (e FindingsFilterFindingFilterAction) ToFindingsFilterFindingFilterActionPtrOutputWithContext(ctx context.Context) FindingsFilterFindingFilterActionPtrOutput {
	return FindingsFilterFindingFilterAction(e).ToFindingsFilterFindingFilterActionOutputWithContext(ctx).ToFindingsFilterFindingFilterActionPtrOutputWithContext(ctx)
}

func (e FindingsFilterFindingFilterAction) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e FindingsFilterFindingFilterAction) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e FindingsFilterFindingFilterAction) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e FindingsFilterFindingFilterAction) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type FindingsFilterFindingFilterActionOutput struct{ *pulumi.OutputState }

func (FindingsFilterFindingFilterActionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FindingsFilterFindingFilterAction)(nil)).Elem()
}

func (o FindingsFilterFindingFilterActionOutput) ToFindingsFilterFindingFilterActionOutput() FindingsFilterFindingFilterActionOutput {
	return o
}

func (o FindingsFilterFindingFilterActionOutput) ToFindingsFilterFindingFilterActionOutputWithContext(ctx context.Context) FindingsFilterFindingFilterActionOutput {
	return o
}

func (o FindingsFilterFindingFilterActionOutput) ToFindingsFilterFindingFilterActionPtrOutput() FindingsFilterFindingFilterActionPtrOutput {
	return o.ToFindingsFilterFindingFilterActionPtrOutputWithContext(context.Background())
}

func (o FindingsFilterFindingFilterActionOutput) ToFindingsFilterFindingFilterActionPtrOutputWithContext(ctx context.Context) FindingsFilterFindingFilterActionPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v FindingsFilterFindingFilterAction) *FindingsFilterFindingFilterAction {
		return &v
	}).(FindingsFilterFindingFilterActionPtrOutput)
}

func (o FindingsFilterFindingFilterActionOutput) ToOutput(ctx context.Context) pulumix.Output[FindingsFilterFindingFilterAction] {
	return pulumix.Output[FindingsFilterFindingFilterAction]{
		OutputState: o.OutputState,
	}
}

func (o FindingsFilterFindingFilterActionOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o FindingsFilterFindingFilterActionOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e FindingsFilterFindingFilterAction) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o FindingsFilterFindingFilterActionOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o FindingsFilterFindingFilterActionOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e FindingsFilterFindingFilterAction) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type FindingsFilterFindingFilterActionPtrOutput struct{ *pulumi.OutputState }

func (FindingsFilterFindingFilterActionPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FindingsFilterFindingFilterAction)(nil)).Elem()
}

func (o FindingsFilterFindingFilterActionPtrOutput) ToFindingsFilterFindingFilterActionPtrOutput() FindingsFilterFindingFilterActionPtrOutput {
	return o
}

func (o FindingsFilterFindingFilterActionPtrOutput) ToFindingsFilterFindingFilterActionPtrOutputWithContext(ctx context.Context) FindingsFilterFindingFilterActionPtrOutput {
	return o
}

func (o FindingsFilterFindingFilterActionPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*FindingsFilterFindingFilterAction] {
	return pulumix.Output[*FindingsFilterFindingFilterAction]{
		OutputState: o.OutputState,
	}
}

func (o FindingsFilterFindingFilterActionPtrOutput) Elem() FindingsFilterFindingFilterActionOutput {
	return o.ApplyT(func(v *FindingsFilterFindingFilterAction) FindingsFilterFindingFilterAction {
		if v != nil {
			return *v
		}
		var ret FindingsFilterFindingFilterAction
		return ret
	}).(FindingsFilterFindingFilterActionOutput)
}

func (o FindingsFilterFindingFilterActionPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o FindingsFilterFindingFilterActionPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *FindingsFilterFindingFilterAction) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// FindingsFilterFindingFilterActionInput is an input type that accepts FindingsFilterFindingFilterActionArgs and FindingsFilterFindingFilterActionOutput values.
// You can construct a concrete instance of `FindingsFilterFindingFilterActionInput` via:
//
//	FindingsFilterFindingFilterActionArgs{...}
type FindingsFilterFindingFilterActionInput interface {
	pulumi.Input

	ToFindingsFilterFindingFilterActionOutput() FindingsFilterFindingFilterActionOutput
	ToFindingsFilterFindingFilterActionOutputWithContext(context.Context) FindingsFilterFindingFilterActionOutput
}

var findingsFilterFindingFilterActionPtrType = reflect.TypeOf((**FindingsFilterFindingFilterAction)(nil)).Elem()

type FindingsFilterFindingFilterActionPtrInput interface {
	pulumi.Input

	ToFindingsFilterFindingFilterActionPtrOutput() FindingsFilterFindingFilterActionPtrOutput
	ToFindingsFilterFindingFilterActionPtrOutputWithContext(context.Context) FindingsFilterFindingFilterActionPtrOutput
}

type findingsFilterFindingFilterActionPtr string

func FindingsFilterFindingFilterActionPtr(v string) FindingsFilterFindingFilterActionPtrInput {
	return (*findingsFilterFindingFilterActionPtr)(&v)
}

func (*findingsFilterFindingFilterActionPtr) ElementType() reflect.Type {
	return findingsFilterFindingFilterActionPtrType
}

func (in *findingsFilterFindingFilterActionPtr) ToFindingsFilterFindingFilterActionPtrOutput() FindingsFilterFindingFilterActionPtrOutput {
	return pulumi.ToOutput(in).(FindingsFilterFindingFilterActionPtrOutput)
}

func (in *findingsFilterFindingFilterActionPtr) ToFindingsFilterFindingFilterActionPtrOutputWithContext(ctx context.Context) FindingsFilterFindingFilterActionPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(FindingsFilterFindingFilterActionPtrOutput)
}

func (in *findingsFilterFindingFilterActionPtr) ToOutput(ctx context.Context) pulumix.Output[*FindingsFilterFindingFilterAction] {
	return pulumix.Output[*FindingsFilterFindingFilterAction]{
		OutputState: in.ToFindingsFilterFindingFilterActionPtrOutputWithContext(ctx).OutputState,
	}
}

// A enumeration value that specifies how frequently finding updates are published.
type SessionFindingPublishingFrequency string

const (
	SessionFindingPublishingFrequencyFifteenMinutes = SessionFindingPublishingFrequency("FIFTEEN_MINUTES")
	SessionFindingPublishingFrequencyOneHour        = SessionFindingPublishingFrequency("ONE_HOUR")
	SessionFindingPublishingFrequencySixHours       = SessionFindingPublishingFrequency("SIX_HOURS")
)

func (SessionFindingPublishingFrequency) ElementType() reflect.Type {
	return reflect.TypeOf((*SessionFindingPublishingFrequency)(nil)).Elem()
}

func (e SessionFindingPublishingFrequency) ToSessionFindingPublishingFrequencyOutput() SessionFindingPublishingFrequencyOutput {
	return pulumi.ToOutput(e).(SessionFindingPublishingFrequencyOutput)
}

func (e SessionFindingPublishingFrequency) ToSessionFindingPublishingFrequencyOutputWithContext(ctx context.Context) SessionFindingPublishingFrequencyOutput {
	return pulumi.ToOutputWithContext(ctx, e).(SessionFindingPublishingFrequencyOutput)
}

func (e SessionFindingPublishingFrequency) ToSessionFindingPublishingFrequencyPtrOutput() SessionFindingPublishingFrequencyPtrOutput {
	return e.ToSessionFindingPublishingFrequencyPtrOutputWithContext(context.Background())
}

func (e SessionFindingPublishingFrequency) ToSessionFindingPublishingFrequencyPtrOutputWithContext(ctx context.Context) SessionFindingPublishingFrequencyPtrOutput {
	return SessionFindingPublishingFrequency(e).ToSessionFindingPublishingFrequencyOutputWithContext(ctx).ToSessionFindingPublishingFrequencyPtrOutputWithContext(ctx)
}

func (e SessionFindingPublishingFrequency) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e SessionFindingPublishingFrequency) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e SessionFindingPublishingFrequency) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e SessionFindingPublishingFrequency) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type SessionFindingPublishingFrequencyOutput struct{ *pulumi.OutputState }

func (SessionFindingPublishingFrequencyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SessionFindingPublishingFrequency)(nil)).Elem()
}

func (o SessionFindingPublishingFrequencyOutput) ToSessionFindingPublishingFrequencyOutput() SessionFindingPublishingFrequencyOutput {
	return o
}

func (o SessionFindingPublishingFrequencyOutput) ToSessionFindingPublishingFrequencyOutputWithContext(ctx context.Context) SessionFindingPublishingFrequencyOutput {
	return o
}

func (o SessionFindingPublishingFrequencyOutput) ToSessionFindingPublishingFrequencyPtrOutput() SessionFindingPublishingFrequencyPtrOutput {
	return o.ToSessionFindingPublishingFrequencyPtrOutputWithContext(context.Background())
}

func (o SessionFindingPublishingFrequencyOutput) ToSessionFindingPublishingFrequencyPtrOutputWithContext(ctx context.Context) SessionFindingPublishingFrequencyPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SessionFindingPublishingFrequency) *SessionFindingPublishingFrequency {
		return &v
	}).(SessionFindingPublishingFrequencyPtrOutput)
}

func (o SessionFindingPublishingFrequencyOutput) ToOutput(ctx context.Context) pulumix.Output[SessionFindingPublishingFrequency] {
	return pulumix.Output[SessionFindingPublishingFrequency]{
		OutputState: o.OutputState,
	}
}

func (o SessionFindingPublishingFrequencyOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o SessionFindingPublishingFrequencyOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e SessionFindingPublishingFrequency) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o SessionFindingPublishingFrequencyOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o SessionFindingPublishingFrequencyOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e SessionFindingPublishingFrequency) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type SessionFindingPublishingFrequencyPtrOutput struct{ *pulumi.OutputState }

func (SessionFindingPublishingFrequencyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SessionFindingPublishingFrequency)(nil)).Elem()
}

func (o SessionFindingPublishingFrequencyPtrOutput) ToSessionFindingPublishingFrequencyPtrOutput() SessionFindingPublishingFrequencyPtrOutput {
	return o
}

func (o SessionFindingPublishingFrequencyPtrOutput) ToSessionFindingPublishingFrequencyPtrOutputWithContext(ctx context.Context) SessionFindingPublishingFrequencyPtrOutput {
	return o
}

func (o SessionFindingPublishingFrequencyPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*SessionFindingPublishingFrequency] {
	return pulumix.Output[*SessionFindingPublishingFrequency]{
		OutputState: o.OutputState,
	}
}

func (o SessionFindingPublishingFrequencyPtrOutput) Elem() SessionFindingPublishingFrequencyOutput {
	return o.ApplyT(func(v *SessionFindingPublishingFrequency) SessionFindingPublishingFrequency {
		if v != nil {
			return *v
		}
		var ret SessionFindingPublishingFrequency
		return ret
	}).(SessionFindingPublishingFrequencyOutput)
}

func (o SessionFindingPublishingFrequencyPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o SessionFindingPublishingFrequencyPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *SessionFindingPublishingFrequency) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// SessionFindingPublishingFrequencyInput is an input type that accepts SessionFindingPublishingFrequencyArgs and SessionFindingPublishingFrequencyOutput values.
// You can construct a concrete instance of `SessionFindingPublishingFrequencyInput` via:
//
//	SessionFindingPublishingFrequencyArgs{...}
type SessionFindingPublishingFrequencyInput interface {
	pulumi.Input

	ToSessionFindingPublishingFrequencyOutput() SessionFindingPublishingFrequencyOutput
	ToSessionFindingPublishingFrequencyOutputWithContext(context.Context) SessionFindingPublishingFrequencyOutput
}

var sessionFindingPublishingFrequencyPtrType = reflect.TypeOf((**SessionFindingPublishingFrequency)(nil)).Elem()

type SessionFindingPublishingFrequencyPtrInput interface {
	pulumi.Input

	ToSessionFindingPublishingFrequencyPtrOutput() SessionFindingPublishingFrequencyPtrOutput
	ToSessionFindingPublishingFrequencyPtrOutputWithContext(context.Context) SessionFindingPublishingFrequencyPtrOutput
}

type sessionFindingPublishingFrequencyPtr string

func SessionFindingPublishingFrequencyPtr(v string) SessionFindingPublishingFrequencyPtrInput {
	return (*sessionFindingPublishingFrequencyPtr)(&v)
}

func (*sessionFindingPublishingFrequencyPtr) ElementType() reflect.Type {
	return sessionFindingPublishingFrequencyPtrType
}

func (in *sessionFindingPublishingFrequencyPtr) ToSessionFindingPublishingFrequencyPtrOutput() SessionFindingPublishingFrequencyPtrOutput {
	return pulumi.ToOutput(in).(SessionFindingPublishingFrequencyPtrOutput)
}

func (in *sessionFindingPublishingFrequencyPtr) ToSessionFindingPublishingFrequencyPtrOutputWithContext(ctx context.Context) SessionFindingPublishingFrequencyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(SessionFindingPublishingFrequencyPtrOutput)
}

func (in *sessionFindingPublishingFrequencyPtr) ToOutput(ctx context.Context) pulumix.Output[*SessionFindingPublishingFrequency] {
	return pulumix.Output[*SessionFindingPublishingFrequency]{
		OutputState: in.ToSessionFindingPublishingFrequencyPtrOutputWithContext(ctx).OutputState,
	}
}

// A enumeration value that specifies the status of the Macie Session.
type SessionStatus string

const (
	SessionStatusEnabled = SessionStatus("ENABLED")
	SessionStatusPaused  = SessionStatus("PAUSED")
)

func (SessionStatus) ElementType() reflect.Type {
	return reflect.TypeOf((*SessionStatus)(nil)).Elem()
}

func (e SessionStatus) ToSessionStatusOutput() SessionStatusOutput {
	return pulumi.ToOutput(e).(SessionStatusOutput)
}

func (e SessionStatus) ToSessionStatusOutputWithContext(ctx context.Context) SessionStatusOutput {
	return pulumi.ToOutputWithContext(ctx, e).(SessionStatusOutput)
}

func (e SessionStatus) ToSessionStatusPtrOutput() SessionStatusPtrOutput {
	return e.ToSessionStatusPtrOutputWithContext(context.Background())
}

func (e SessionStatus) ToSessionStatusPtrOutputWithContext(ctx context.Context) SessionStatusPtrOutput {
	return SessionStatus(e).ToSessionStatusOutputWithContext(ctx).ToSessionStatusPtrOutputWithContext(ctx)
}

func (e SessionStatus) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e SessionStatus) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e SessionStatus) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e SessionStatus) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type SessionStatusOutput struct{ *pulumi.OutputState }

func (SessionStatusOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SessionStatus)(nil)).Elem()
}

func (o SessionStatusOutput) ToSessionStatusOutput() SessionStatusOutput {
	return o
}

func (o SessionStatusOutput) ToSessionStatusOutputWithContext(ctx context.Context) SessionStatusOutput {
	return o
}

func (o SessionStatusOutput) ToSessionStatusPtrOutput() SessionStatusPtrOutput {
	return o.ToSessionStatusPtrOutputWithContext(context.Background())
}

func (o SessionStatusOutput) ToSessionStatusPtrOutputWithContext(ctx context.Context) SessionStatusPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SessionStatus) *SessionStatus {
		return &v
	}).(SessionStatusPtrOutput)
}

func (o SessionStatusOutput) ToOutput(ctx context.Context) pulumix.Output[SessionStatus] {
	return pulumix.Output[SessionStatus]{
		OutputState: o.OutputState,
	}
}

func (o SessionStatusOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o SessionStatusOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e SessionStatus) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o SessionStatusOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o SessionStatusOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e SessionStatus) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type SessionStatusPtrOutput struct{ *pulumi.OutputState }

func (SessionStatusPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SessionStatus)(nil)).Elem()
}

func (o SessionStatusPtrOutput) ToSessionStatusPtrOutput() SessionStatusPtrOutput {
	return o
}

func (o SessionStatusPtrOutput) ToSessionStatusPtrOutputWithContext(ctx context.Context) SessionStatusPtrOutput {
	return o
}

func (o SessionStatusPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*SessionStatus] {
	return pulumix.Output[*SessionStatus]{
		OutputState: o.OutputState,
	}
}

func (o SessionStatusPtrOutput) Elem() SessionStatusOutput {
	return o.ApplyT(func(v *SessionStatus) SessionStatus {
		if v != nil {
			return *v
		}
		var ret SessionStatus
		return ret
	}).(SessionStatusOutput)
}

func (o SessionStatusPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o SessionStatusPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *SessionStatus) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// SessionStatusInput is an input type that accepts SessionStatusArgs and SessionStatusOutput values.
// You can construct a concrete instance of `SessionStatusInput` via:
//
//	SessionStatusArgs{...}
type SessionStatusInput interface {
	pulumi.Input

	ToSessionStatusOutput() SessionStatusOutput
	ToSessionStatusOutputWithContext(context.Context) SessionStatusOutput
}

var sessionStatusPtrType = reflect.TypeOf((**SessionStatus)(nil)).Elem()

type SessionStatusPtrInput interface {
	pulumi.Input

	ToSessionStatusPtrOutput() SessionStatusPtrOutput
	ToSessionStatusPtrOutputWithContext(context.Context) SessionStatusPtrOutput
}

type sessionStatusPtr string

func SessionStatusPtr(v string) SessionStatusPtrInput {
	return (*sessionStatusPtr)(&v)
}

func (*sessionStatusPtr) ElementType() reflect.Type {
	return sessionStatusPtrType
}

func (in *sessionStatusPtr) ToSessionStatusPtrOutput() SessionStatusPtrOutput {
	return pulumi.ToOutput(in).(SessionStatusPtrOutput)
}

func (in *sessionStatusPtr) ToSessionStatusPtrOutputWithContext(ctx context.Context) SessionStatusPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(SessionStatusPtrOutput)
}

func (in *sessionStatusPtr) ToOutput(ctx context.Context) pulumix.Output[*SessionStatus] {
	return pulumix.Output[*SessionStatus]{
		OutputState: in.ToSessionStatusPtrOutputWithContext(ctx).OutputState,
	}
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FindingsFilterFindingFilterActionInput)(nil)).Elem(), FindingsFilterFindingFilterAction("ARCHIVE"))
	pulumi.RegisterInputType(reflect.TypeOf((*FindingsFilterFindingFilterActionPtrInput)(nil)).Elem(), FindingsFilterFindingFilterAction("ARCHIVE"))
	pulumi.RegisterInputType(reflect.TypeOf((*SessionFindingPublishingFrequencyInput)(nil)).Elem(), SessionFindingPublishingFrequency("FIFTEEN_MINUTES"))
	pulumi.RegisterInputType(reflect.TypeOf((*SessionFindingPublishingFrequencyPtrInput)(nil)).Elem(), SessionFindingPublishingFrequency("FIFTEEN_MINUTES"))
	pulumi.RegisterInputType(reflect.TypeOf((*SessionStatusInput)(nil)).Elem(), SessionStatus("ENABLED"))
	pulumi.RegisterInputType(reflect.TypeOf((*SessionStatusPtrInput)(nil)).Elem(), SessionStatus("ENABLED"))
	pulumi.RegisterOutputType(AllowListStatusOutput{})
	pulumi.RegisterOutputType(AllowListStatusPtrOutput{})
	pulumi.RegisterOutputType(FindingsFilterFindingFilterActionOutput{})
	pulumi.RegisterOutputType(FindingsFilterFindingFilterActionPtrOutput{})
	pulumi.RegisterOutputType(SessionFindingPublishingFrequencyOutput{})
	pulumi.RegisterOutputType(SessionFindingPublishingFrequencyPtrOutput{})
	pulumi.RegisterOutputType(SessionStatusOutput{})
	pulumi.RegisterOutputType(SessionStatusPtrOutput{})
}
