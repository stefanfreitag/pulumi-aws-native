// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.
 */
export class ScheduledAudit extends pulumi.CustomResource {
    /**
     * Get an existing ScheduledAudit resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ScheduledAudit {
        return new ScheduledAudit(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iot:ScheduledAudit';

    /**
     * Returns true if the given object is an instance of ScheduledAudit.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ScheduledAudit {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ScheduledAudit.__pulumiType;
    }

    /**
     * The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.
     */
    public readonly dayOfMonth!: pulumi.Output<string | undefined>;
    /**
     * The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.
     */
    public readonly dayOfWeek!: pulumi.Output<enums.iot.ScheduledAuditDayOfWeek | undefined>;
    /**
     * How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.
     */
    public readonly frequency!: pulumi.Output<enums.iot.ScheduledAuditFrequency>;
    /**
     * The ARN (Amazon resource name) of the scheduled audit.
     */
    public /*out*/ readonly scheduledAuditArn!: pulumi.Output<string>;
    /**
     * The name you want to give to the scheduled audit.
     */
    public readonly scheduledAuditName!: pulumi.Output<string | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * Which checks are performed during the scheduled audit. Checks must be enabled for your account.
     */
    public readonly targetCheckNames!: pulumi.Output<string[]>;

    /**
     * Create a ScheduledAudit resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ScheduledAuditArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.frequency === undefined) && !opts.urn) {
                throw new Error("Missing required property 'frequency'");
            }
            if ((!args || args.targetCheckNames === undefined) && !opts.urn) {
                throw new Error("Missing required property 'targetCheckNames'");
            }
            resourceInputs["dayOfMonth"] = args ? args.dayOfMonth : undefined;
            resourceInputs["dayOfWeek"] = args ? args.dayOfWeek : undefined;
            resourceInputs["frequency"] = args ? args.frequency : undefined;
            resourceInputs["scheduledAuditName"] = args ? args.scheduledAuditName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["targetCheckNames"] = args ? args.targetCheckNames : undefined;
            resourceInputs["scheduledAuditArn"] = undefined /*out*/;
        } else {
            resourceInputs["dayOfMonth"] = undefined /*out*/;
            resourceInputs["dayOfWeek"] = undefined /*out*/;
            resourceInputs["frequency"] = undefined /*out*/;
            resourceInputs["scheduledAuditArn"] = undefined /*out*/;
            resourceInputs["scheduledAuditName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["targetCheckNames"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["scheduledAuditName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ScheduledAudit.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ScheduledAudit resource.
 */
export interface ScheduledAuditArgs {
    /**
     * The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.
     */
    dayOfMonth?: pulumi.Input<string>;
    /**
     * The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.
     */
    dayOfWeek?: pulumi.Input<enums.iot.ScheduledAuditDayOfWeek>;
    /**
     * How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.
     */
    frequency: pulumi.Input<enums.iot.ScheduledAuditFrequency>;
    /**
     * The name you want to give to the scheduled audit.
     */
    scheduledAuditName?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * Which checks are performed during the scheduled audit. Checks must be enabled for your account.
     */
    targetCheckNames: pulumi.Input<pulumi.Input<string>[]>;
}
