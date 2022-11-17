// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudtrail

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 90 to 2555 days (about three months to up to seven years).
type EventDataStore struct {
	pulumi.CustomResourceState

	// The advanced event selectors that were used to select events for the data store.
	AdvancedEventSelectors EventDataStoreAdvancedEventSelectorArrayOutput `pulumi:"advancedEventSelectors"`
	// The timestamp of the event data store's creation.
	CreatedTimestamp pulumi.StringOutput `pulumi:"createdTimestamp"`
	// The ARN of the event data store.
	EventDataStoreArn pulumi.StringOutput `pulumi:"eventDataStoreArn"`
	// Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
	KmsKeyId pulumi.StringPtrOutput `pulumi:"kmsKeyId"`
	// Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
	MultiRegionEnabled pulumi.BoolPtrOutput `pulumi:"multiRegionEnabled"`
	// The name of the event data store.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// Indicates that an event data store is collecting logged events for an organization.
	OrganizationEnabled pulumi.BoolPtrOutput `pulumi:"organizationEnabled"`
	// The retention period, in days.
	RetentionPeriod pulumi.IntPtrOutput `pulumi:"retentionPeriod"`
	// The status of an event data store. Values are ENABLED and PENDING_DELETION.
	Status pulumi.StringOutput          `pulumi:"status"`
	Tags   EventDataStoreTagArrayOutput `pulumi:"tags"`
	// Indicates whether the event data store is protected from termination.
	TerminationProtectionEnabled pulumi.BoolPtrOutput `pulumi:"terminationProtectionEnabled"`
	// The timestamp showing when an event data store was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.
	UpdatedTimestamp pulumi.StringOutput `pulumi:"updatedTimestamp"`
}

// NewEventDataStore registers a new resource with the given unique name, arguments, and options.
func NewEventDataStore(ctx *pulumi.Context,
	name string, args *EventDataStoreArgs, opts ...pulumi.ResourceOption) (*EventDataStore, error) {
	if args == nil {
		args = &EventDataStoreArgs{}
	}

	var resource EventDataStore
	err := ctx.RegisterResource("aws-native:cloudtrail:EventDataStore", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEventDataStore gets an existing EventDataStore resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEventDataStore(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EventDataStoreState, opts ...pulumi.ResourceOption) (*EventDataStore, error) {
	var resource EventDataStore
	err := ctx.ReadResource("aws-native:cloudtrail:EventDataStore", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EventDataStore resources.
type eventDataStoreState struct {
}

type EventDataStoreState struct {
}

func (EventDataStoreState) ElementType() reflect.Type {
	return reflect.TypeOf((*eventDataStoreState)(nil)).Elem()
}

type eventDataStoreArgs struct {
	// The advanced event selectors that were used to select events for the data store.
	AdvancedEventSelectors []EventDataStoreAdvancedEventSelector `pulumi:"advancedEventSelectors"`
	// Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
	MultiRegionEnabled *bool `pulumi:"multiRegionEnabled"`
	// The name of the event data store.
	Name *string `pulumi:"name"`
	// Indicates that an event data store is collecting logged events for an organization.
	OrganizationEnabled *bool `pulumi:"organizationEnabled"`
	// The retention period, in days.
	RetentionPeriod *int                `pulumi:"retentionPeriod"`
	Tags            []EventDataStoreTag `pulumi:"tags"`
	// Indicates whether the event data store is protected from termination.
	TerminationProtectionEnabled *bool `pulumi:"terminationProtectionEnabled"`
}

// The set of arguments for constructing a EventDataStore resource.
type EventDataStoreArgs struct {
	// The advanced event selectors that were used to select events for the data store.
	AdvancedEventSelectors EventDataStoreAdvancedEventSelectorArrayInput
	// Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
	KmsKeyId pulumi.StringPtrInput
	// Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
	MultiRegionEnabled pulumi.BoolPtrInput
	// The name of the event data store.
	Name pulumi.StringPtrInput
	// Indicates that an event data store is collecting logged events for an organization.
	OrganizationEnabled pulumi.BoolPtrInput
	// The retention period, in days.
	RetentionPeriod pulumi.IntPtrInput
	Tags            EventDataStoreTagArrayInput
	// Indicates whether the event data store is protected from termination.
	TerminationProtectionEnabled pulumi.BoolPtrInput
}

func (EventDataStoreArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*eventDataStoreArgs)(nil)).Elem()
}

type EventDataStoreInput interface {
	pulumi.Input

	ToEventDataStoreOutput() EventDataStoreOutput
	ToEventDataStoreOutputWithContext(ctx context.Context) EventDataStoreOutput
}

func (*EventDataStore) ElementType() reflect.Type {
	return reflect.TypeOf((**EventDataStore)(nil)).Elem()
}

func (i *EventDataStore) ToEventDataStoreOutput() EventDataStoreOutput {
	return i.ToEventDataStoreOutputWithContext(context.Background())
}

func (i *EventDataStore) ToEventDataStoreOutputWithContext(ctx context.Context) EventDataStoreOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EventDataStoreOutput)
}

type EventDataStoreOutput struct{ *pulumi.OutputState }

func (EventDataStoreOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EventDataStore)(nil)).Elem()
}

func (o EventDataStoreOutput) ToEventDataStoreOutput() EventDataStoreOutput {
	return o
}

func (o EventDataStoreOutput) ToEventDataStoreOutputWithContext(ctx context.Context) EventDataStoreOutput {
	return o
}

// The advanced event selectors that were used to select events for the data store.
func (o EventDataStoreOutput) AdvancedEventSelectors() EventDataStoreAdvancedEventSelectorArrayOutput {
	return o.ApplyT(func(v *EventDataStore) EventDataStoreAdvancedEventSelectorArrayOutput {
		return v.AdvancedEventSelectors
	}).(EventDataStoreAdvancedEventSelectorArrayOutput)
}

// The timestamp of the event data store's creation.
func (o EventDataStoreOutput) CreatedTimestamp() pulumi.StringOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.StringOutput { return v.CreatedTimestamp }).(pulumi.StringOutput)
}

// The ARN of the event data store.
func (o EventDataStoreOutput) EventDataStoreArn() pulumi.StringOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.StringOutput { return v.EventDataStoreArn }).(pulumi.StringOutput)
}

// Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
func (o EventDataStoreOutput) KmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.StringPtrOutput { return v.KmsKeyId }).(pulumi.StringPtrOutput)
}

// Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
func (o EventDataStoreOutput) MultiRegionEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.BoolPtrOutput { return v.MultiRegionEnabled }).(pulumi.BoolPtrOutput)
}

// The name of the event data store.
func (o EventDataStoreOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// Indicates that an event data store is collecting logged events for an organization.
func (o EventDataStoreOutput) OrganizationEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.BoolPtrOutput { return v.OrganizationEnabled }).(pulumi.BoolPtrOutput)
}

// The retention period, in days.
func (o EventDataStoreOutput) RetentionPeriod() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.IntPtrOutput { return v.RetentionPeriod }).(pulumi.IntPtrOutput)
}

// The status of an event data store. Values are ENABLED and PENDING_DELETION.
func (o EventDataStoreOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

func (o EventDataStoreOutput) Tags() EventDataStoreTagArrayOutput {
	return o.ApplyT(func(v *EventDataStore) EventDataStoreTagArrayOutput { return v.Tags }).(EventDataStoreTagArrayOutput)
}

// Indicates whether the event data store is protected from termination.
func (o EventDataStoreOutput) TerminationProtectionEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.BoolPtrOutput { return v.TerminationProtectionEnabled }).(pulumi.BoolPtrOutput)
}

// The timestamp showing when an event data store was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.
func (o EventDataStoreOutput) UpdatedTimestamp() pulumi.StringOutput {
	return o.ApplyT(func(v *EventDataStore) pulumi.StringOutput { return v.UpdatedTimestamp }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EventDataStoreInput)(nil)).Elem(), &EventDataStore{})
	pulumi.RegisterOutputType(EventDataStoreOutput{})
}
